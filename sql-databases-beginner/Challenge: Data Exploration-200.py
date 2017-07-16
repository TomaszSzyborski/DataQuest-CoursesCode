## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]

## 2. Find Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]
minimums = "select min(population), min(population_growth), min(birth_rate), min(death_rate) from facts;"
maximums = "select max(population), max(population_growth), max(birth_rate), max(death_rate) from facts;"
min_results = conn.execute(minimums).fetchall()
max_results = conn.execute(maximums).fetchall()

# population column
pop_min = min_results[0][0]
pop_max = max_results[0][0]
# population_growth column
pop_growth_min = min_results[0][1]
pop_growth_max = max_results[0][1]
# birth_rate column
birth_rate_min = min_results[0][2]
birth_rate_max = max_results[0][2]
# death_rate column
death_rate_min = min_results[0][3]
death_rate_max = max_results[0][3]

print(min_results)
print(max_results)

## 3. Filter Values ##

conn = sqlite3.connect("factbook.db")
min_and_max = '''
select min(population), max(population), min(population_growth), max(population_growth),
min(birth_rate), max(birth_rate), min(death_rate), max(death_rate)
from facts where population > 0 and population < 2000000000;
'''
results = conn.execute(min_and_max).fetchall()
print(results)

# population column
pop_min = results[0][0]
pop_max = results[0][1]
# population_growth column
pop_growth_min = results[0][2]
pop_growth_max = results[0][3]
# birth_rate column
birth_rate_min = results[0][4]
birth_rate_max = results[0][5]
# death_rate column
death_rate_min = results[0][6]
death_rate_max = results[0][7]

## 4. Predict Future Population Growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")
projected_population_query = '''
select round(population + population * (population_growth/100), 0) from facts
where population > 0 and population < 7000000000 
and population is not null and population_growth is not null;
'''

projected_population = conn.execute(projected_population_query).fetchall()

print(projected_population[0:10])

## 5. Explore Projected Population ##

import sqlite3
conn = sqlite3.connect("factbook.db")
proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)