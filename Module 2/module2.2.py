import pandas as pd
import networkx as nx

g = nx.Graph()

airports = pd.read_csv("mod2_airport_name.csv")
routes = pd.read_csv("mod2_route_names.csv")

for _, row in airports.iterrows():
    g.add_node(row['Airport ID'], name=row['Name'], city=row['City'], country=row['Country'])

for _, row in routes.iterrows():
    source_id = row['Source airport ID']
    dest_id = row['Destination airport ID']
    if source_id in g.nodes and dest_id in g.nodes:
        g.add_edge(source_id, dest_id)
    else:
        # Found some missing values, so adding placeholder values in placed needed
        if source_id not in g.nodes:
            g.add_node(source_id, name='Unknown', city='Unknown', country='Unknown')
        if dest_id not in g.nodes:
            g.add_node(dest_id, name='Unknown', city='Unknown', country='Unknown')
        g.add_edge(source_id, dest_id)

traffic_degree = g.degree()

us_airports = [(airport_id, degree) for airport_id, degree in traffic_degree if g.nodes[airport_id]['country'] == 'United States']
sorted_us_airports = sorted(us_airports, key=lambda x: x[1], reverse=True)

print("Top 10 US Airports by Connectivity:")
for airport_id, degree in sorted_us_airports[:10]:
    airport_name = g.nodes[airport_id]['name']
    city = g.nodes[airport_id]['city']
    print(f"{airport_name} (ID: {airport_id}, City: {city}): {degree}")
