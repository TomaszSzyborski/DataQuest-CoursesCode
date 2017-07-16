## 2. Hash Tables ##

import os
quotes = {}
directory = "lines"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        quotes[filename.replace(".txt", "")] = f.read()

## 3. Hash Functions ##

def simple_hash(key):
    pass
def simple_hash(key):
    key = str(key)
    return ord(key[0])

xmen_hash = simple_hash("xmen")
things_hash = simple_hash("10thingsihateaboutyou")

## 4. Fitting Values Into An Array ##

def simple_hash(key):
    key = str(key)
    return ord(key[0])
def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

xmen_hash = simple_hash("xmen")
things_hash = simple_hash("10thingsihateaboutyou")

## 5. Creating A Hash Table ##

import numpy as np

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

class HashTable():
    
    def __init__(self, size):
        pass
    
    def __getitem__(self, key):
        pass
    
    def __setitem__(self, key, value):
        pass
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        self.array[ind] = value

hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()

## 6. Hash Collisions ##

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        self.array[ind] = value
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append(value)

hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()

with open("lines/xmenoriginswolverine.txt", 'r') as f:
    hash_table["xmenoriginswolverine"] = f.read()

## 7. Retrieving Values From Hash Tables ##

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append(value)
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append((key,value))
        
hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()

with open("lines/xmenoriginswolverine.txt", 'r') as f:
    hash_table["xmenoriginswolverine"] = f.read()

## 8. Overwriting Values ##

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append((key,value))
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()

with open("lines/xmenoriginswolverine.txt", 'r') as f:
    hash_table["xmen"] = f.read()

## 9. Profiling Hash Tables ##

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 1

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

data = [
    ("xmen", "Wolverine"), 
    ("xmenoriginswolverine", "Superman"), 
    ("vanillasky", "Thor"), 
    ("tremors", "Aquaman")
]
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        counter = 0
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            counter += 1
            if key == k:
                return counter
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

hash_table = HashTable(1)
for k,v in data:
    hash_table[k] = v

counter = hash_table[k]

## 10. Profiling Array Length ##

import time
import os
import matplotlib.pyplot as plt

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

def profile_table(size):
    hash_table = HashTable(size)
    directory = "lines"
    
    for filename in os.listdir(directory):
        name = filename.replace(".txt", "")
        hash_table[name] = quotes[name]

lengths = [1,10,20,30,40,50]
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = hash(key) % self.size
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = hash(key) % self.size
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

def profile_table(size):
    start = time.time()
    hash_table = HashTable(size)
    directory = "lines"
    
    for filename in os.listdir(directory):
        name = filename.replace(".txt", "")
        hash_table[name] = quotes[name]
    
    duration = time.time() - start
    return duration

times = []
for l in lengths:
    times.append(profile_table(l))

plt.plot(lengths, times)