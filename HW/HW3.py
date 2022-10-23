import pandas as pd
import numpy as np

# A
data_path = 'https://data.gov.ua/dataset/d0f0755f-ce75-4d6b-8310-6e4ddf320c11/resource/0a385ec9-f85e-499c-980e' \
            '-37accb04d8d5/download/reimbursement_legal_entity_divisions_info.csv'
df = pd.read_csv(data_path, sep=',', header=None)
df.columns = df.iloc[0]
df = df.drop(axis='index', index=0)
df.reset_index(drop=True, inplace=True)
# B
print(df.info())
# C
print(df.shape)
# D and E
df.loc[df['legal_entity_edrpou'] == 'ФОП', 'legal_entity_edrpou'] = 0
df = df.astype({'legal_entity_edrpou': 'int64', 'legal_entity_inserted_at': 'datetime64'})
print(df.info())
# F
city_filter = df['division_settlement_type'] == 'місто'
city_count = df[city_filter].value_counts(subset=['division_settlement'])
print(city_count)
# G
df.drop('division_settlement', axis=1, inplace=True)
print(df.info())
# H
unique_val = df['division_type'].value_counts()
print(unique_val)
# I
x = ['legal_entity_edrpou', 'legal_entity_inserted_at']
new_df = df.iloc[1:2000, 0:6]
print(new_df)
# J
df = df.astype({'lng': 'float'})
east_f = df.loc[df['lng'] == df['lng'].max(axis=0)]
print(east_f)
# K
df = df.astype({'lat': 'float'})
filter_df = df['lat'] < 50
lat_df = df[filter_df]
lat_df = lat_df.loc[:, 'legal_entity_name']
print(lat_df)
# L
df.drop_duplicates(inplace=True, ignore_index=True)
# df.reset_index(drop=True, inplace=True)
print(df)
