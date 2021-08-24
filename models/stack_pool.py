class StackPool:
    def __init__(self):
        self.values = [0] * 1000
        self.current_index_first = -1
        self.current_index_second = -1
        self.current_index_third = -1

    def push_first(self, value):
        if self.current_index_first < 0:
            self.current_index_first = 0
        self.values[self.current_index_first] = value
        self.current_index_first += 3

    def pop_first(self):
        if self.current_index_first < 0:
            raise ValueError
        value = self.values[self.current_index_first]
        self.current_index_first -= 3
        return value

    def push_second(self, value):
        if self.current_index_second < 0:
            self.current_index_second = 1
        self.values[self.current_index_second] = value
        self.current_index_second += 3

    def pop_second(self):
        if self.current_index_second < 0:
            raise ValueError
        value = self.values[self.current_index_second]
        self.current_index_second -= 3
        return value

    def push_third(self, value):
        if self.current_index_third < 0:
            self.current_index_third = 2
        self.values[self.current_index_third] = value
        self.current_index_third += 3

    def pop_third(self):
        if self.current_index_third < 0:
            raise ValueError
        value = self.values[self.current_index_third]
        self.current_index_third -= 3
        return value
