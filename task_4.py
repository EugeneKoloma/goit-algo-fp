import uuid
import argparse
import networkx as nx
import matplotlib.pyplot as plt


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


def draw_tree(tree_root, title=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(9, 6))
    if title:
        plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def build_heap_tree(arr):
    if not arr:
        return None
    nodes = [None if v is None else Node(v) for v in arr]
    n = len(nodes)
    for i in range(n):
        if nodes[i] is None:
            continue
        li, ri = 2*i + 1, 2*i + 2
        if li < n and nodes[li] is not None:
            nodes[i].left = nodes[li]
        if ri < n and nodes[ri] is not None:
            nodes[i].right = nodes[ri]
    return nodes[0]


def visualize_heap(arr):
    root = build_heap_tree(arr)
    if root is None:
        print("Empty heap")
        return
    draw_tree(root, title="Binary Heap as Tree")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize binary heap (array) as a binary tree")
    parser.add_argument("values", nargs="*", type=int, help="Heap values in array order")
    args = parser.parse_args()
    if args.values:
        visualize_heap(args.values)
    else:
        # demo min-heap array
        heap_array = [1, 3, 2, 7, 8, 5, 4, 9]
        visualize_heap(heap_array)
