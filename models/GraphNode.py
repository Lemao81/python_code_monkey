from typing import Sequence


class GraphNode:
    def __init__(self):
        self.adjacent = []
        self.visited = False
