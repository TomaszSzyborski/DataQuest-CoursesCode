## 2. Defining the Dataset Class ##


class Dataset:
    def __init__(self):
        self.type = "csv"

dataset = Dataset()
print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

class Dataset:
    def __init__(self):
        self.type = "csv"
class Dataset:
    def __init__(self, data):
        self.data = data

f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

## 4. Adding Additional Behavior ##

class Dataset:
    def __init__(self, data):
        self.data = data
        
    # Your method goes here
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def print_data(self, num_rows):
        print(self.data[:num_rows])


nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

class Dataset:
    def __init__(self, data):
        self.data = data

nfl_dataset = Dataset(nfl_data)
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

## 6. Grabbing Column Data ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.

nfl_dataset = Dataset(nfl_data)
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

## 7. Count Unique Method ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    # Add your count unique method here

nfl_dataset = Dataset(nfl_data)
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def count_unique(self, label):
        count = 0
        for item in set(self.column(label)):
            count += 1
        return count

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

## 8. Make Objects Human Readable ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # Add the special method here
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
    def count_unique(self, label):
        count = 0
        for item in set(self.column(label)):
            count += 1
        return count

nfl_dataset = Dataset(nfl_data)
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def __str__(self):
        data_string = self.data[:10]
        return str(data_string)
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def count_unique(self, label):
        count = 0
        for item in set(self.column(label)):
            count += 1
        return count

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)