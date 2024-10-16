# -*- coding: utf-8 -*-
"""Module3.1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BQJER-5aebyaKOZdBYfTIxXbT97RwZ8b
"""

import pandas as pd
from sklearn.metrics import pairwise_distances, jaccard_score
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans


airports = pd.read_csv("mod2_airport_name.csv")
routes = pd.read_csv("mod2_route_names.csv")

# print(routes.head(10))

temp = airports[['Country']]
# print(temp)
temp_airports = temp.groupby('Country').value_counts().reset_index()
temp_airports.columns = ['Country', 'Airport_Count']
temp_airports.set_index('Country', inplace = True)
# print(temp_airports)

query_country = "India"
query_value = temp_airports.loc[query_country].values.reshape(-1, 1)
air_temp = temp_airports['Airport_Count'].values.reshape(-1, 1)

euc_dist = pairwise_distances(air_temp, query_value, metric='euclidean')

distance_df = pd.DataFrame({
    'Country': temp_airports.index,
    'Distance': euc_dist.flatten()
})

sorted_distance_df = distance_df.sort_values(by='Distance')
euc_top_10 = sorted_distance_df.head(10)
print("Countries with similar number of airport to India:")
print(euc_top_10)