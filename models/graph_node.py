class GraphNode:
    def __init__(self, value):
        self.value = value
        self.adjacent = []
        self.visited = False

    def __str__(self):
        return str(self.value)
