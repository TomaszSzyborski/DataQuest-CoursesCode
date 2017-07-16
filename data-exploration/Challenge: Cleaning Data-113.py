## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers['Year']>=1960]

## 5. Consolidating Deaths ##

#selecting interesting columns
deaths = true_avengers[["Death1","Death2","Death3","Death4","Death5"]]

# filling NaNs with "NO"
deaths = deaths.fillna("NO")
deaths_count = deaths.apply(pd.Series.value_counts, axis=1).fillna(0)

true_avengers["Deaths"] = deaths_count["YES"]

print(true_avengers.head(3))

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
ref_year = 2015
years_since_joining = ref_year - true_avengers["Year"]

correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)