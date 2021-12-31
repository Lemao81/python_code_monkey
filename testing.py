import common
from models.graph_node import GraphNode
from functools import cmp_to_key
from typing import List


def compare_dependencies(first: GraphNode, second: GraphNode):
    print(list(map(lambda x: x.value, [first, second])))
    if len(first.adjacent) == 0 and len(second.adjacent) == 0:
        return 0
    if len(first.adjacent) > 0 and len(second.adjacent) == 0:
        return 1 if second in first.adjacent else 0
    if len(first.adjacent) == 0 and len(second.adjacent) > 0:
        return -1 if first in second.adjacent else 0
    if len(first.adjacent) > 0 and len(second.adjacent) > 0:
        if first in second.adjacent and second in first.adjacent:
            raise ValueError('Cycle dependency')
        if first in second.adjacent:
            return -1
        if second in first.adjacent:
            return 1
        return 0
    raise ValueError('Inconsistent')


def sort_graphs(unsorted: List, sorted: List):
    without_links = list(filter(lambda x: len(x.adjacent) == 0, unsorted))
    if len(without_links) == 0:
        raise ValueError()
    for graph in without_links:
        sorted.append(graph)
        unsorted.remove(graph)
        for graph2 in unsorted:
            if graph in graph2.adjacent:
                graph2.adjacent.remove(graph)

    if len(unsorted) > 0:
        sort_graphs(unsorted, sorted)

    return sorted


if __name__ == '__main__':
    graph_a = GraphNode('a')
    graph_b = GraphNode('b')
    graph_c = GraphNode('c')
    graph_d = GraphNode('d')
    graph_e = GraphNode('e')
    graph_f = GraphNode('f')

    graph_d.adjacent.append(graph_a)
    graph_b.adjacent.append(graph_f)
    graph_d.adjacent.append(graph_b)
    graph_a.adjacent.append(graph_f)
    graph_c.adjacent.append(graph_d)

    graphs = [graph_a, graph_b, graph_c, graph_d, graph_e, graph_f]
    graphs_sorted2 = []
    sort_graphs(graphs, graphs_sorted2)
    print(list(map(lambda x: x.value, graphs_sorted2)))

    # graphs_sorted = sorted(graphs, key=cmp_to_key(compare_dependencies))
    # print(list(map(lambda x: x.value, graphs_sorted)))
