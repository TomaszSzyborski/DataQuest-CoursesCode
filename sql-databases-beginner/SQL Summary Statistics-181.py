## 1. Introduction ##


import sqlite3

conn = sqlite3.connect("factbook.db")
facts = conn.execute("SELECT * FROM facts;").fetchall()
print(facts)
facts_count = len(facts)

## 2. Counting the Number of Rows in SQL ##

conn = sqlite3.connect("factbook.db")
birth_rate_tuple = conn.execute("SELECT COUNT(birth_rate) FROM facts;").fetchall()
birth_rate_count = birth_rate_tuple[0][0]
print(birth_rate_count)

## 3. Finding a Column's Minimum and Maximum Values in SQL ##

conn = sqlite3.connect("factbook.db")
pop_growth_tuple = conn.execute("SELECT MIN(population_growth) FROM facts;").fetchall()
min_population_growth = pop_growth_tuple[0][0]
print(min_population_growth)

death_rate_tuple = conn.execute("SELECT MAX(death_rate) FROM facts;").fetchall()
max_death_rate = death_rate_tuple[0][0]
print(max_death_rate)

## 4. Calculating Sums and Averages in SQL ##

conn = sqlite3.connect("factbook.db")
total_land_tuple = conn.execute("SELECT SUM(area_land) FROM facts;").fetchall()
total_land_area = total_land_tuple[0][0]
print(total_land_area)

avg_water_tuple = conn.execute("SELECT AVG(area_water) FROM facts;").fetchall()
avg_water_area = avg_water_tuple[0][0]
print(avg_water_area)

## 5. Combining Multiple Aggregation Functions ##

conn = sqlite3.connect("factbook.db")
facts_stats = conn.execute("SELECT AVG(population), SUM(population), MAX(birth_rate) FROM facts;").fetchall()
mean_pop = facts_stats[0][0]
sum_pop = facts_stats[0][1]
max_birth_rate = facts_stats[0][2]

## 6. Aggregating Values for a Subset of the Data ##

conn = sqlite3.connect("factbook.db")
pop_query = conn.execute("SELECT AVG(population_growth) FROM facts WHERE population > 10000000;").fetchall()
population_growth = pop_query[0][0]
print(population_growth)

## 7. Selecting Unique Rows ##

conn = sqlite3.connect("factbook.db")
unique_birth_rates = conn.execute("SELECT DISTINCT birth_rate FROM facts;").fetchall()
print(unique_birth_rates)

## 8. Aggregating Unique Values ##

conn = sqlite3.connect("factbook.db")
query = conn.execute("SELECT AVG(DISTINCT birth_rate) FROM facts WHERE population > 20000000;").fetchall()
average_birth_rate = query[0][0]
print(average_birth_rate)

query = conn.execute("SELECT SUM(DISTINCT population) FROM facts WHERE area_land > 1000000;").fetchall()
sum_population = query[0][0]
print(sum_population)

## 9. Performing Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
population_growth_millions = conn.execute("SELECT population_growth / 1000000.0 FROM facts;").fetchall()
print(population_growth_millions)

## 10. Performing Arithmetic Between Columns ##

conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute("SELECT (1 + (population_growth/100)) * population FROM facts;").fetchall()
print(next_year_population)