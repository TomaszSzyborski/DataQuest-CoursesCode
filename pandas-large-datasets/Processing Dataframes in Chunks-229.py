## 2. Processing Chunks ##

import pandas as pd
import matplotlib.pyplot as plt

memory_footprints = []
chunk_iter = pd.read_csv("moma.csv", chunksize=250)
for chunk in chunk_iter:
    memory_footprints.append(chunk.memory_usage(deep=True).sum()/(1024*1024))

plt.hist(memory_footprints)
plt.show()

## 3. Counting Across Chunks ##

num_rows = 0
chunk_iter = pd.read_csv("moma.csv", chunksize=250)
for chunk in chunk_iter:
    num_rows += len(chunk)
print(num_rows)

## 4. Batch Processing ##

dtypes = {"ConstituentBeginDate": "float", "ConstituentEndDate": "float"}
chunk_iter = pd.read_csv("moma.csv", chunksize=250, dtype=dtypes)
lifespans = []
for chunk in chunk_iter:
    diff = chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate']
    lifespans.append(diff)
lifespans_dist = pd.concat(lifespans)
print(lifespans_dist)

## 6. Counting Unique Values ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = list()
for chunk in chunk_iter:
    chunk_vc = chunk['Gender'].value_counts()
    overall_vc.append(chunk_vc)
combined_vc = pd.concat(overall_vc)
print(combined_vc)

## 7. Combining Chunks Using GroupBy ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = list()
for chunk in chunk_iter:
    chunk_vc = chunk['Gender'].value_counts()
    overall_vc.append(chunk_vc)
combined_vc = pd.concat(overall_vc)
final_vc = combined_vc.groupby(combined_vc.index).sum()
print(final_vc)

## 8. Working With Intermediate Dataframes ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250)
df_list = []
for chunk in chunk_iter:
    temp = chunk['Gender'].groupby(chunk['ExhibitionID']).value_counts()
    df_list.append(temp)
final_df = pd.concat(df_list)
id_gender_counts = final_df.groupby(final_df.index).sum()