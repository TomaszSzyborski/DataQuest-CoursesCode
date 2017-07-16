## 3. Read the File Into a String ##

with open("dq_unisex_names.csv", "r") as f:
    names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[:5]

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = [name.split(',') for name in names_list]

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for i in nested_list:
    v = i[0]
    f = float(i[1])
    nl = [v,f]
    numerical_list.append(nl)