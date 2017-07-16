## 2. Sorting Arrays ##

import pandas as pd
from statistics import mean

data = pd.read_csv("amounts.csv")
amounts = list(data["Amount"])
times = list(data["Time"])

print(mean(amounts))

## 3. Swapping Elements ##


def swap(array, pos1, pos2):
    store = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = store

first_amounts = amounts[:10]
swap(first_amounts, 1,2)

## 4. Selection Sort ##


def selection_sort(array):
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)

first_amounts = amounts[:10]
selection_sort(first_amounts)

## 5. Profiling The Selection Sort ##

import matplotlib.pyplot as plt

def selection_sort(array):
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)

lengths = [10,100,1000,10000]
def selection_sort(array):
    counter = 0
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            counter += 1
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)
    return counter


counters = []
for i in lengths:
    first_amounts = amounts[:i]
    counter = selection_sort(first_amounts)
    counters.append(counter)

plt.plot(lengths, counters)

## 6. Bubble Sort ##


def bubble_sort(array):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1

first_amounts = amounts[:10]
bubble_sort(first_amounts)

## 7. Profiling The Bubble Sort ##

import matplotlib.pyplot as plt

def bubble_sort(array):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1

lengths = [10,100,1000,10000]
def bubble_sort(array):
    swaps = 1
    counter = 0
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            counter += 1
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1
    return counter

counters = []
for i in lengths:
    first_amounts = amounts[:i]
    counter = bubble_sort(first_amounts)
    counters.append(counter)

plt.plot(lengths, counters)

## 9. Insertion Sort ##


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

first_amounts = amounts[:10]
insertion_sort(first_amounts)

## 10. Profiling The Insertion Sort ##

import matplotlib.pyplot as plt

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

lengths = [10,100,1000,10000]
def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1
            counter += 1
    return counter

counters = []
for i in lengths:
    first_amounts = amounts[:i]
    counter = insertion_sort(first_amounts)
    counters.append(counter)

plt.plot(lengths, counters)