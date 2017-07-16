## 2. Introduction ##

import pandas as pd

moma = pd.read_csv("moma.csv")
print(moma.info())

## 3. How Pandas Represents Values in a Dataframe ##

import pandas as pd
moma = pd.read_csv("moma.csv")

print(moma._data)

## 5. Different Types Have Different Memory Footprints ##

total_bytes = moma.size * 8
total_megabytes = total_bytes / (1024*1024)

print(total_bytes)
print(total_megabytes)

## 7. Calculating the True Memory Footprint ##

obj_cols = moma.select_dtypes(include=["object"])
#print(obj_cols)

obj_cols_mem = obj_cols.memory_usage(deep=True)
print(obj_cols_mem)

obj_cols_sum = obj_cols_mem.sum() / 1048576
print(obj_cols_sum)

## 9. Optimizing Integer Columns With Subtypes ##

import numpy as np

def optimize_integers_with_subtypes(data_frame, column_name):
    col_max = data_frame[column_name].max()
    col_min = data_frame[column_name].min()
    integer_subtypes = ["int8", "int16", "int32", "int64"]
    for subtype in integer_subtypes:
        if col_max < np.iinfo(subtype).max and col_min > np.iinfo(subtype).min:
            data_frame[column_name] = data_frame[column_name].astype(subtype)
            break
    print(data_frame[column_name].dtype)
    print(data_frame[column_name].memory_usage(deep=True))
    

optimize_integers_with_subtypes(moma, "ExhibitionSortOrder")

## 10. Optimizing Float Columns With Subtypes ##

import numpy as np

moma = pd.read_csv("moma.csv")
moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
float_cols = moma.select_dtypes(include=['float'])
print(float_cols.dtypes)

for col in float_cols.columns:
    moma[col] = pd.to_numeric(moma[col], downcast='float')

print(moma.select_dtypes(include=['float']).dtypes)

## 12. Converting To DateTime ##

names_to_convert = ["ExhibitionBeginDate", "ExhibitionEndDate"]

for name in names_to_convert:
    print("{0} Before conversion: {1}".format(name, moma[name].memory_usage(deep=True)))
    moma[name] = pd.to_datetime(moma[name])
    print("{0} After conversion: {1}".format(name, moma[name].memory_usage(deep=True)))
    
print(moma[names_to_convert].memory_usage(deep=True))

## 14. Converting to Categorical to Save Memory ##

obj_cols = moma.select_dtypes(include=['object'])
print("Before conversion: {}".format(moma.info(memory_usage='deep')))

for col in obj_cols.columns:
    num_unique_values = len(moma[col].unique())
    num_total_values = len(moma[col])
    if num_unique_values / num_total_values < 0.5:
        moma[col] = moma[col].astype('category')
        
print("\n\n\nAfter conversion: {}".format(moma.info(memory_usage='deep')))

## 15. Selecting Types While Reading the Data In ##

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']

moma = pd.read_csv("moma.csv", usecols=keep_cols, parse_dates =["ExhibitionBeginDate", "ExhibitionEndDate"])

print(moma.info(memory_usage="deep"))