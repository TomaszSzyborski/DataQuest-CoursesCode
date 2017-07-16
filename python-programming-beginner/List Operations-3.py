## 2. Parsing the File ##

weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for row in weather_data:
    weather.append(row[1])

## 4. Counting the Items in a List ##

count = 0
count = len(weather)

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for w in weather_types:
    weather_type_found.append(w in new_weather)