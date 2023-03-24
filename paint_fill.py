SCREEN_WIDTH = 30
SCREEN_HEIGHT = 20


def is_in_screen(point: tuple[int, int], screen: list[list[int]]):
    rows_count = len(screen)
    return rows_count > 0 and 0 <= point[1] < rows_count and 0 <= point[0] < len(screen[0])


def fill_paint_recursive(point: tuple[int, int], old_color: int, new_color: int, screen: list[list[int]]):
    if not is_in_screen(point, screen):
        return
    x, y = point
    screen[y][x] = new_color
    for x1 in range(x - 1, x + 2):
        for y1 in range(y - 1, y + 2):
            if is_in_screen((x1, y1), screen) and screen[y1][x1] == old_color:
                fill_paint_recursive((x1, y1), old_color, new_color, screen)


def print_screen(screen: list[list[int]]):
    for row in screen:
        for x in row:
            print(x, end=' ')
        print()


def draw_straight_line(p1: tuple[int, int], p2: tuple[int, int], color: int, screen: list[list[int]]):
    if not is_in_screen(p1, screen) or not is_in_screen(p2, screen) or not (p1[0] == p2[0] or p1[1] == p2[1]):
        return
    for y in range(p1[0], p2[0] + 1):
        for x in range(p1[1], p2[1] + 1):
            screen[y][x] = color


screen = list()
old_color = 14
for y in range(SCREEN_HEIGHT):
    row = list()
    for x in range(SCREEN_WIDTH):
        row.append(old_color)
    screen.append(row)

new_color = 77
print_screen(screen)
draw_straight_line((3, 4), (3, 17), 99, screen)
draw_straight_line((3, 4), (8, 4), 99, screen)
draw_straight_line((8, 4), (8, 17), 99, screen)
draw_straight_line((3, 17), (8, 17), 99, screen)
print()
print_screen(screen)
# fill_paint_recursive((13, 5), old_color, new_color, screen, list())
fill_paint_recursive((22, 3), old_color, new_color, screen)
print()
print_screen(screen)
