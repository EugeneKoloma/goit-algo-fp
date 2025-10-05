import uuid
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors_map=None, title=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    colors = []
    for node_id, data in tree.nodes(data=True):
        if colors_map and node_id in colors_map:
            colors.append(colors_map[node_id])
        else:
            colors.append(data.get('color', 'skyblue'))
    plt.figure(figsize=(9, 6))
    if title:
        plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def gradient(n, base=(18, 150, 240), end=(220, 240, 255)):
    if n <= 0:
        return []
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        r = int(base[0] + (end[0] - base[0]) * t)
        g = int(base[1] + (end[1] - base[1]) * t)
        b = int(base[2] + (end[2] - base[2]) * t)
        out.append(f"#{r:02x}{g:02x}{b:02x}")
    return out


def dfs_order(root):
    if not root:
        return []
    order = []
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop()
        if node.id in visited:
            continue
        visited.add(node.id)
        order.append(node)
        # push right then left to visit left first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs_order(root):
    if not root:
        return []
    order = []
    q = deque([root])
    visited = set([root.id])
    while q:
        node = q.popleft()
        order.append(node)
        for child in (node.left, node.right):
            if child and child.id not in visited:
                visited.add(child.id)
                q.append(child)
    return order


if __name__ == "__main__":
    # sample tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    dfs_nodes = dfs_order(root)
    bfs_nodes = bfs_order(root)

    dfs_colors = {n.id: c for n, c in zip(dfs_nodes, gradient(len(dfs_nodes), base=(18, 150, 240), end=(230, 240, 255)))}
    bfs_colors = {n.id: c for n, c in zip(bfs_nodes, gradient(len(bfs_nodes), base=(30, 80, 30), end=(200, 240, 200)))}

    draw_tree(root, dfs_colors, title="DFS order coloring")
    draw_tree(root, bfs_colors, title="BFS order coloring")
