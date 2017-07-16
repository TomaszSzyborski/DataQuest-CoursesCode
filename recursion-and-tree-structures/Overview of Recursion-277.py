## 2. Recursion is thinking in Recursion ##


search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']

def search(strings, term, index=0):
    if strings[0] == term:
        return index
    if len(strings) <= 1:
        return -1
    return search(strings[1:], term, index=index+1)

apple_index = search(search_list, 'apple')
pear_index = search(search_list, 'pear')
foo_index = search(search_list, 'foo')

## 3. Stack Overflow ##

def traverse_list(values):
    return traverse_list(values)

traverse_list([])

## 4. Divide and Conquer ##

# Load your file and cast it to integers here.

f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

def summation(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]

    midpoint = len(values) // 2
    return summation(values[:midpoint]) + summation(values[midpoint:])   

divide_and_conquer_sum = summation(random_integers)

## 6. Merge Sort (Part 2) ##

f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

def merge_sort(unsorted):
    # Implement the recursion logic here.
    # You can use the `merge` function described in the example from
    # Part 1.
    sorted = merge([], [])
    return sorted
f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    
    midpoint = len(unsorted) // 2
    left_side = merge_sort(unsorted[:midpoint])
    right_side = merge_sort(unsorted[midpoint:])
    
    sorted = merge(left_side, right_side)
    return sorted

random_sorted = merge_sort(random_integers)