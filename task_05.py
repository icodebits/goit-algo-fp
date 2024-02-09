import uuid
import networkx as nx
import matplotlib.pyplot as plt

from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)  # Використання id та збереження значення вузла
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

def depth_first_traversal(node, colors):
    if node is None:
        return
    colors[node.id] = generate_color(len(colors), 'dft')
    depth_first_traversal(node.left, colors)
    depth_first_traversal(node.right, colors)

def breadth_first_traversal(node, colors):
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        colors[current_node.id] = generate_color(len(colors), 'bft')
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

def generate_color(index, traversal_type):
    # Генерування колірного коду у форматі #RRGGBB
    color_intensity = hex(int(255 * (index * 30 / 256)))[2:]
    return f"#{color_intensity.zfill(2)}{color_intensity.zfill(2)}{color_intensity.zfill(2)}"

def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    title = ''
    if traversal_type == 'depth_first':
        depth_first_traversal(tree_root, colors)
        title = "Depth First Traversal"
    elif traversal_type == 'breadth_first':
        breadth_first_traversal(tree_root, colors)
        title = "Breadth First Traversal"

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    draw_colors = []
    for key, _ in labels.items():
        draw_colors.append(colors[key])

    plt.figure(figsize=(8, 8))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, font_color="#FF0000", font_weight="bold", font_size=22, arrows=False, node_size=2500, node_color=draw_colors)
    plt.show()

if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева з обходом у глибину
    draw_tree(root, 'depth_first')

    # Відображення дерева з обходом у ширину
    draw_tree(root, 'breadth_first')
