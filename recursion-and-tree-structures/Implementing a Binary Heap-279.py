## 2. Heap Inserts ##

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        # Helpful method to keep track of Node values.
        return "<Node: {}>".format(self.value)    

class MaxHeap:
    def __init__(self):
        self.root = None
    
    # Implement your `insert` method here.
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return "<Node: {}>".format(self.value)

class MaxHeap:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        node = Node(value=value)
        if not self.root:
            self.root = node
            return node
        
        if self.root.value >= node.value:
            # Normal insert.
            node.parent = self.root
            if not self.root.left:
                self.root.left = node
            elif not self.root.right:
                self.root.right = node
            return node
        # Swap the nodes.
        old_root = self.root
        node.left = old_root.left
        node.right = old_root.right
        self.root = node
        
        if not self.root.left:
            self.root.left = old_root
        elif not self.root.right:
            self.root.right = old_root
        return node

heap = MaxHeap()
heap.insert(3)
heap.insert(9)
heap.insert(11)
root = heap.root.value
left = heap.root.left.value 
right = heap.root.right.value

## 3. Speed Up Insert ##

# We don't need to use the `Node` class anymore.

class MaxHeap:
    def __init__(self):
        self.nodes = []
    
    # Add your new `insert` method here.
    
heap = MaxHeap()
class MaxHeap:
    def __init__(self):
        self.nodes = []
    
    def insert(self, value):
        self.nodes.append(value)
        index = len(self.nodes) - 1
        parent_index = math.floor((index-1)/2)
        
        while index > 0 and self.nodes[parent_index] < self.nodes[index]:
            self.nodes[parent_index], self.nodes[index] = self.nodes[index], self.nodes[parent_index]
            index = parent_index
            parent_index = math.floor((index-1)/2)
        return self.nodes
    
heap = MaxHeap()
heap.insert(3)
heap.insert(9)
heap.insert(11)
nodes = heap.nodes

## 4. Get the Max Integer ##

class MaxHeap(BaseMaxHeap):
    pass

    # Add your methods here.
    
heap = MaxHeap()
class MaxHeap(BaseMaxHeap):
    def insert_multiple(self, values):
        for value in values:
            self.insert(value)

    def max(self):
        return self.nodes[0]
    
heap = MaxHeap()
heap.insert_multiple(heap_list)
heap_max = heap.max()

## 5. Pop the Root Value ##

class MaxHeap(BaseMaxHeap):
    pass
    # Add your methods here.
    
heap = MaxHeap()
class MaxHeap(BaseMaxHeap):
    def pop(self):
        root = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes = self.nodes[:-1]
        index = 0
        left_child_idx = 2*index + 1
        right_child_idx = 2*index + 2
        
        while max(left_child_idx, right_child_idx) < len(self.nodes) - 1:
            swap_index = left_child_idx
            if self.nodes[left_child_idx] < self.nodes[right_child_idx]:
                swap_index = right_child_idx
                
            if self.nodes[swap_index] < self.nodes[index]:
                return root
            
            self.nodes[swap_index], self.nodes[index] = self.nodes[index], self.nodes[swap_index]
            index = swap_index
            left_child_idx = 2*index + 1
            right_child_idx = 2*index + 2
        return root
    
    
heap = MaxHeap()
heap.insert_multiple(heap_list)
heap_max = heap.pop()

## 6. Grab the Top N Elements ##

class MaxHeap(BaseMaxHeap):
    pass
    
    # Add your method here.
    
heap = MaxHeap()
class MaxHeap(BaseMaxHeap):
    def top_n_elements(self, n):
        return [self.pop() for _ in range(n)]
    
heap = MaxHeap()
heap.insert_multiple(heap_list)
top_100 = heap.top_n_elements(1000)

## 7. Using Python's Heap ##

with open('amounts.csv', 'r') as f:
    reader = csv.reader(f)
    heap_list = list(reader)[1:]
    
top_100 = heapq.nlargest(100, heap_list, key=lambda x: x[1])

## 8. Analyzing the Heap ##

heap_list = list(range(10 * 100 * 5000))
random.shuffle(heap_list)
    
start = time.time()
sorted(heap_list, reverse=True)[:100]
print("Sorting search took: {} seconds".format(time.time() - start))

start = time.time()
heapq.nlargest(100, heap_list)
print("Heap search took: {} seconds".format(time.time() - start))