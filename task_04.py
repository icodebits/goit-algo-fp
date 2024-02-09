import uuid

import heapq
import networkx as nx
import matplotlib.pyplot as plt

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, key):
        heapq.heappush(self.heap, key)

    def pop(self):
        return heapq.heappop(self.heap)

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap(keys):
    heap = BinaryHeap()
    for key in keys:
        heap.push(key)

    root = Node(heap.pop())
    current_level = [root]
    while heap.heap:
        next_level = []
        for node in current_level:
            if heap.heap:
                node.left = Node(heap.pop())
                next_level.append(node.left)
            if heap.heap:
                node.right = Node(heap.pop())
                next_level.append(node.right)
        current_level = next_level

    return root

if __name__ == "__main__":
    # Створення бінарної купи
    keys = [0, 4, 5, 10, 1, 3]
    heap_root = build_heap(keys)

    # Відображення бінарної купи
    draw_heap(heap_root)
