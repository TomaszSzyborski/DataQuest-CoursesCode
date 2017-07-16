## 1. Introduction ##

# `csv` and `BTree` are given to you.
with open('amounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    values = [float(l[0]) for l in reader]

btree = BTree(5)
btree.insert_multiple(values)

search = btree.search(btree.root, 17116)
root = btree.root.keys

## 2. Enhance the Node ##

# `csv` and `BTree` are given to you.
btree = BTree(5)
class NodeKey:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __repr__(self):
        return '<NodeKey: ({}, {})>'.format(self.key, self.value)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key
        return self.key == other
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.key > other.key
        return self.key > other
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.key >= other.key
        return self.key >= other
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.key < other.key
        return self.key < other
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.key <= other.key
        return self.key <= other
        
with open('amounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    nodekeys = [NodeKey(float(l[0]), float(l[0])) for l in reader]

btree = BTree(5)
btree.insert_multiple(nodekeys)
search = btree.search(btree.root, 171116)
root_key = btree.root.keys[0].key

## 3. Parsing the Data ##

with open('amounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    nodekeys = [NodeKey(float(l[0]), reader.line_num) for l in reader]

btree = BTree(5)
btree.insert_multiple(nodekeys)
root_value = btree.root.keys[1].value

## 4. Reworking the Search Method ##

class BTreeIndex(BTree):
    def search(self, node, term):
        if not self.root:
            return False
        index = 0
        for key in node.keys:
            if key == term:
                return True
            if term > key:
                index += 1
        if node.is_leaf():
            return False
        return self.search(node.children[index], term)

index = BTreeIndex(5)
index.insert_multiple(nodekeys)
class BTreeIndex(BTree):
    def search(self, node, term):
        if not self.root:
            return None
        index = 0
        for key in node.keys:
            if key == term:
                return key.value
            if term > key:
                index += 1
        if node.is_leaf():
            return None
        return self.search(node.children[index], term)
    
index = BTreeIndex(5)
index.insert_multiple(nodekeys)
search_1 = index.search(btree.root, 171116)
search_2 = index.search(btree.root, 100000000)

## 5. Implementing the Range Query ##

class BTreeIndex(BaseBTreeIndex):
    def greater_than(self):
        return None

index = BTreeIndex(5)
#index.insert_multiple(nodekeys)
class BTreeIndex(BaseBTreeIndex):
    def greater_than(self, node, term, upper_bound=None, inclusive=False):
        if not self.root:
            return []
        index = 0
        values = []
        for key in node.keys:
            if upper_bound is not None:
                if inclusive and key == upper_bound:
                    values.append(key)
                if key >= upper_bound:
                    break
            if term > key:
                index += 1
                continue
            if inclusive and key == term:
                values.append(key)
            if key > term:
                values.append(key)
            if not node.is_leaf():
                values += self.greater_than(
                    node.children[index],
                    term,
                    upper_bound,
                    inclusive
                )
            index += 1
        if not node.is_leaf():
            values += self.greater_than(
                node.children[index],
                term,
                upper_bound,
                inclusive
            )
        return values
        
index = BTreeIndex(5)
index.insert_multiple(nodekeys)
greater = index.greater_than(index.root, 170361)
other_greater = index.greater_than(index.root, 170361)
upper = index.greater_than(index.root, 170361, upper_bound=171409)
inclusive = index.greater_than(index.root, 170361, upper_bound=171409, inclusive=True)

## 6. Add an Additional Range Query ##

class BTreeIndex(BaseBTreeIndex):
    def less_than(self):
        return None

index = BTreeIndex(5)
#index.insert_multiple(nodekeys)
class BTreeIndex(BaseBTreeIndex):
    def less_than(self, node, term, lower_bound=None, inclusive=False):
        if not self.root:
            return []
        index = 0
        values = []
        for key in node.keys:
            if lower_bound is not None:
                if inclusive and key == lower_bound:
                    values.append(key)
                if key < lower_bound:
                    index += 1
                    continue
            if inclusive and key == term:
                values.append(key)
            if key < term:
                values.append(key)
            if not node.is_leaf():
                values += self.less_than(
                    node.children[index],
                    term,
                    lower_bound,
                    inclusive
                )
            index += 1
                
        if not node.is_leaf() and key <= term:
            values += self.less_than(
                node.children[index],
                term,
                lower_bound,
                inclusive
            )
        return values
        
index = BTreeIndex(5)
index.insert_multiple(nodekeys)
less_than = index.less_than(index.root, 769)
lower = index.less_than(index.root, 769, lower_bound=46)
inclusive = index.less_than(index.root, 769, lower_bound=46, inclusive=True)

## 7. Saving our Model ##

import pickle
import pickle
        
index = BTreeIndex(4)
index.insert_multiple(nodekeys)
with open('index_example.pickle', 'wb') as f:
    pickle.dump(index, f)

with open('index_example.pickle', 'rb') as f:
    index_new = pickle.load(f)

new_key = index_new.root.keys[0].key