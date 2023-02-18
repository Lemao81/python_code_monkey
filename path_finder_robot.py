from enum import Enum


class Direction(Enum):
    UNKNOWN = 0
    LEFT = 1
    TOP = 2
    RIGHT = 3
    DOWN = 4


def get_favoured_to_directions(from_direction: Direction) -> list[Direction]:
    match from_direction:
        case Direction.UNKNOWN:
            return [Direction.RIGHT, Direction.DOWN]
        case Direction.LEFT:
            return [Direction.RIGHT, Direction.DOWN, Direction.TOP, Direction.LEFT]
        case Direction.TOP:
            return [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.TOP]
        case Direction.RIGHT:
            return [Direction.DOWN, Direction.LEFT, Direction.TOP, Direction.RIGHT]
        case Direction.DOWN:
            return [Direction.RIGHT, Direction.LEFT, Direction.TOP, Direction.DOWN]


def get_opposite_direction(direction: Direction) -> Direction:
    match direction:
        case Direction.UNKNOWN:
            raise ValueError('Direction.UNKNOWN has no opposite direction')
        case Direction.LEFT:
            return Direction.RIGHT
        case Direction.TOP:
            return Direction.DOWN
        case Direction.RIGHT:
            return Direction.LEFT
        case Direction.DOWN:
            return Direction.TOP


def get_coordinates_after_move(to_direction: Direction, current_row_index: int, current_column_index: int) -> (int, int):
    match to_direction:
        case Direction.UNKNOWN:
            raise ValueError('case Direction.UNKNOWN not valid here')
        case Direction.LEFT:
            return current_row_index, current_column_index - 1
        case Direction.TOP:
            return current_row_index - 1, current_column_index
        case Direction.RIGHT:
            return current_row_index, current_column_index + 1
        case Direction.DOWN:
            return current_row_index + 1, current_column_index


class Grid():
    def __init__(self, row_count: int, column_count: int):
        self._row_count = row_count
        self._column_count = column_count
        self._blocks = dict[int, list[int]]()
        self._touches = dict[int, list[int]]()
        self.max_row_index = row_count - 1
        self.max_column_index = column_count - 1

    def is_inside(self, row_index: int, column_index: int):
        return 0 <= row_index < self._row_count and 0 <= column_index < self._column_count

    def is_blocked(self, row_index: int, column_index: int):
        if row_index not in self._blocks:
            return False
        blocked_column_indices = self._blocks[row_index]
        return column_index in blocked_column_indices

    def is_touched(self, row_index: int, column_index: int):
        if row_index not in self._touches:
            return False
        touched_column_indices = self._touches[row_index]
        return column_index in touched_column_indices

    def is_reachable(self, row_index: int, column_index: int):
        return self.is_inside(row_index, column_index) and not self.is_blocked(row_index, column_index)

    def visualize(self):
        header_row_string = '    '
        for column_index in range(self._column_count):
            header_row_string += f' {column_index}  '
        print(header_row_string)

        for row_index in range(self._row_count):
            row_string = f'{row_index}  |'
            for column_index in range(self._column_count):
                if self.is_blocked(row_index, column_index):
                    column_string = ' X |'
                elif self.is_touched(row_index, column_index):
                    column_string = ' + |'
                else:
                    column_string = '   |'
                row_string += column_string
            print(row_string)

    def add_block(self, row_index: int, column_index: int):
        if row_index not in self._blocks:
            self._blocks[row_index] = [column_index]
        self._blocks[row_index].append(column_index)

    def add_touch(self, row_index: int, column_index: int):
        if row_index not in self._touches:
            self._touches[row_index] = [column_index]
        self._touches[row_index].append(column_index)


class Robot():
    def __init__(self, grid: Grid):
        self.steps = 0
        self._grid = grid
        self._current_from_direction = Direction.UNKNOWN
        self._current_row_index = 0
        self._current_column_index = 0
        self._grid.add_touch(0, 0)
        self._moves = dict[(int, int), list[Direction]]()
        print(
            f'Starting from {self._get_current_position_string()}, need to go to {self._get_position_string(self._grid.max_row_index, self._grid.max_column_index)}')

    def check_direction(self, direction: Direction) -> bool:
        pass

    def move(self):
        continue_trying = True
        while continue_trying and (self._current_row_index < self._grid.max_row_index or self._current_column_index < self._grid.max_column_index):
            favoured_move_directions = get_favoured_to_directions(self._current_from_direction)
            moved = False
            for to_direction in favoured_move_directions:
                target_row_index, target_column_index = get_coordinates_after_move(to_direction, self._current_row_index, self._current_column_index)
                is_repeated_move = self._is_repeated_move(target_row_index, target_column_index, to_direction)
                if is_repeated_move:
                    continue
                is_reachable = self._grid.is_reachable(target_row_index, target_column_index)
                if is_reachable:
                    self._current_row_index = target_row_index
                    self._current_column_index = target_column_index
                    print(f'Moved to {self._get_current_position_string()}')
                    self._grid.add_touch(self._current_row_index, self._current_column_index)
                    self._current_from_direction = get_opposite_direction(to_direction)
                    self.steps += 1
                    moved = True
                    moves_key = (target_row_index, target_column_index)
                    if moves_key not in self._moves:
                        self._moves[moves_key] = []
                    self._moves[moves_key].append(to_direction)
                    break
            if not moved:
                continue_trying = False
        if continue_trying:
            print('FINAL DESTINATION REACHED :)')
            print(f'Took me {self.steps} steps')
        else:
            print('FINAL DESTINATION UNREACHABLE :(')
            print(f'Tried {self.steps} steps')

    def _is_repeated_move(self, row_index: int, column_index: int, to_direction: Direction):
        key = (row_index, column_index)
        if key == (0, 0):
            return True
        elif key not in self._moves:
            return False
        return to_direction in self._moves[key]

    def _get_current_position_string(self):
        return self._get_position_string(self._current_row_index, self._current_column_index)

    @staticmethod
    def _get_position_string(row_index: int, column_index: int):
        return f'({row_index} / {column_index})'


grid = Grid(5, 5)
grid.add_block(2, 4)
grid.add_block(2, 3)
grid.add_block(3, 2)
grid.add_block(3, 3)
# grid.add_block(4, 3)
grid.add_block(2, 1)
grid.visualize()
print()
print()
robot = Robot(grid)
robot.move()
print()
print()
grid.visualize()
