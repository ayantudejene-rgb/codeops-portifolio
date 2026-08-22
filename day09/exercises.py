from collections import deque
import heapq
#Exercise 1: 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    """Insert a value into a BST, returning the (possibly new) root."""
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def inorder(root):
    """In-order traversal of BST – returns sorted list."""
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

balances = [800, 200, 1200, 400, 1600, 600]
root = None
for b in balances:
    root = insert(root, b)
print("BST in-order (sorted):", inorder(root))

# Exercise 2: 
def height(node):
    """Return the height of a binary tree (max depth)."""
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

print("Height of BST:", height(root))

#Exercise 3: 
def bfs(graph, start):
    """Return set of reachable vertices from start using BFS."""
    visited = {start}
    q = deque([start])
    while q:
        v = q.popleft()
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return visited

# Exercise 4:
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

sample_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS from A:", bfs(sample_graph, 'A'))
print("DFS from A:", dfs_recursive(sample_graph, 'A'))

#Exercise 5:
tasks = [(3, "Email"), (1, "Emergency"), (4, "Report"), (2, "Meeting"), (5, "Break")]
heap = []
for priority, task in tasks:
    heapq.heappush(heap, (priority, task))
print("Popping tasks by priority:")
while heap:
    priority, task = heapq.heappop(heap)
    print(f"  {priority}: {task}")