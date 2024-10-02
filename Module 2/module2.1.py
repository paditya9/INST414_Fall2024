import pandas as pd
import networkx as nx

g = nx.Graph()

airports = pd.read_csv("mod2_airport_name.csv")
routes = pd.read_csv("mod2_route_names.csv")


for _, row in airports.iterrows():
    g.add_node(row['Airport ID'], name=row['Name'], city=row['City'], country=row['Country'])

for _, row in routes.iterrows():
    g.add_edge(row['Source airport ID'], row['Destination airport ID'])


traffic_degree = g.degree()

sorted_trafiic = sorted(traffic_degree, key = lambda x:x[1], reverse=True)

print("Top 20 Airports by Connectivity across the world:")
for airport_id, degree in sorted_trafiic[:20]:
    airport_name = g.nodes[airport_id]['name']
    city = g.nodes[airport_id]['city']
    print(f"{airport_name} (ID: {airport_id}, City: {city}): {degree}")