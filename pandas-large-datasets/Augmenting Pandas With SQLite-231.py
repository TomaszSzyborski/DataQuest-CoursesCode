## 1. Augmenting Pandas With SQLite ##

import sqlite3
import pandas as pd
conn = sqlite3.connect('moma.db')
moma_iter = pd.read_csv('moma.csv', chunksize=1000)
for chunk in moma_iter:
    chunk.to_sql("exhibitions", conn, if_exists='append', index=False)

## 2. Pandas Types vs. SQLite Types ##

results_df = pd.read_sql('PRAGMA table_info(exhibitions);', conn)
print(results_df)

## 3. Setting Appropriate Types ##

moma_iter = pd.read_csv('moma.csv', chunksize=1000)
for chunk in moma_iter:
    chunk['ExhibitionSortOrder'] = chunk['ExhibitionSortOrder'].astype('int16')
    chunk.to_sql("exhibitions", conn, if_exists='append', index=False)
results_df = pd.read_sql('PRAGMA table_info(exhibitions);', conn)
print(results_df)

## 4. Computing Primarily in SQL ##

q = 'select exhibitionid, count(*) as counts from exhibitions group by exhibitionid order by counts desc;'
eid_counts = pd.read_sql(q, conn)
print(eid_counts[:10])

## 5. Computing Primarily in Pandas ##

q = 'select exhibitionid from exhibitions;'
eid_df = pd.read_sql(q, conn)
eid_pandas_counts = eid_df['ExhibitionID'].value_counts()
print(eid_pandas_counts[:10])