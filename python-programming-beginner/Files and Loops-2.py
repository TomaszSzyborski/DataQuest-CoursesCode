## 2. Opening Files ##

f = open("crime_rates.csv", "r")
print(f)

## 3. Reading In Files ##

f = open("crime_rates.csv", "r")
data=f.read()

## 4. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

## 6. Practice - Loops ##

ten_rows = rows[0:10]
for row in ten_rows:
    print(row)

## 8. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = [row.split(',') for row in rows]
#for row in rows:
#    row.split(',')
print(final_data)

## 9. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list = [entry[0] for entry in five_elements]

## 10. Looping Through a List of Lists ##

crime_rates = []
cities_list = [entry[0] for entry in final_data]

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)

## 11. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

int_crime_rates = []

for row in rows:
    # row is a list variable, not a string.
    r = row.split(',')
    crime_rate = int(r[1])
    # crime_rate is a string, the crime rate of the city.
    int_crime_rates.append(crime_rate)