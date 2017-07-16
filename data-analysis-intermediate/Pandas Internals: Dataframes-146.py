## 1. Shared Indexes ##

import pandas as pd
fandango = pd.read_csv('fandango_score_comparison.csv')
print(fandango.head(2))
print(fandango.index)

## 2. Using Integer Indexes to Select Rows ##

fandango = pd.read_csv('fandango_score_comparison.csv')
first_row = 0
last_row = fandango.shape[0] - 1
first_last = fandango.iloc[[first_row, last_row]]

## 3. Using Custom Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films = fandango.set_index('FILM', drop=False)
print(fandango_films.index)

## 4. Using a Custom Index for Selection ##

movies = ["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[movies]

## 6. Apply() Logic Over Columns: Practice ##

double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))
halved_df = float_df.apply(lambda x: x/2)
print(halved_df.head(1))

## 7. Apply() Over Dataframe Rows ##

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print(rt_mt_means[0:5])