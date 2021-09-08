import random

from models.graph_node import GraphNode
from models.queue import Queue


def find_breadth_first(node1: GraphNode, node2: GraphNode) -> bool:
    queue = Queue[GraphNode]()
    queue.enqueue(node1)

    while not queue.is_empty():
        node = queue.dequeue()
        if node is node2:
            return True
        else:
            not_visited = list(filter(lambda x: not x.visited, node.adjacent))
            a: GraphNode
            for a in not_visited:
                if a is node2:
                    return True
            for a in not_visited:
                queue.enqueue(a)
                a.visited = True
    return False


def find_depth_first(node: GraphNode, node2: GraphNode) -> bool:
    node.visited = True
    for a in filter(lambda x: not x.visited, node.adjacent):
        if find_depth_first(a, node2):
            return True
    if node is node2:
        return True
    return False


if __name__ == '__main__':
    node1 = GraphNode(random.randint)
    node1_1 = GraphNode(random.randint)
    node1.adjacent.append(GraphNode(random.randint))
    node1.adjacent.append(GraphNode(random.randint))
    node1.adjacent.append(node1_1)
    node1.adjacent.append(GraphNode(random.randint))
    node2 = GraphNode(random.randint)
    node1_1.adjacent.append(GraphNode(random.randint))
    node1_1.adjacent.append(GraphNode(random.randint))
    node1_1.adjacent.append(node2)
    node1_1.adjacent.append(GraphNode(random.randint))
    node1_1.adjacent.append(GraphNode(random.randint))

    found1 = find_breadth_first(node1, node2)
    # found2 = find_depth_first(node1, node2)

    print('FOUND' if found1 else 'NOT FOUND')
    # print('FOUND' if found2 else 'NOT FOUND')
