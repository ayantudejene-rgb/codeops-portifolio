# day07/practice.py

import time
from collections import deque
#Exercise 2: 
def time_lookup(structure, key):
    start = time.perf_counter()
    _ = structure.get(key) if isinstance(structure, dict) else (key in structure)
    return time.perf_counter() - start

size = 100_000
keys = [f"ACC-{i:05d}" for i in range(size)]
test_key = keys[-1] 
lst = keys.copy()
list_time = time_lookup(lst, test_key)
d = {k: None for k in keys}
dict_time = time_lookup(d, test_key)

print(f"List lookup time: {list_time:.6f}s")
print(f"Dict lookup time: {dict_time:.6f}s")

#Exercise 3: 
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
names = ["Almaz", "Dawit", "Tigist", "Hanna"]
s = Stack()
for name in names:
    s.push(name)
reversed_names = []
while not s.is_empty():
    reversed_names.append(s.pop())
print("Original:", names)
print("Reversed:", reversed_names)

#Exercise 4: 
def bank_queue():
    q = deque()
    # Enqueue five customers
    customers = ["A", "B", "C", "D", "E"]
    for c in customers:
        q.append(c)
        print(f"{c} joined the queue.")
    # Serve them in order
    print("Serving:")
    while q:
        served = q.popleft()
        print(f"Serving {served}")

bank_queue()

#Exercise 5:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")
ll = LinkedList()
ll.push_front("Tigist")
ll.push_front("Dawit")
ll.push_front("Almaz")
ll.print_all()  