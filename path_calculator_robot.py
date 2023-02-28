GRID_MAX_R = 10
GRID_MAX_C = 10


def is_off_limit(r: int, c: int) -> bool:
    return r > GRID_MAX_R or c > GRID_MAX_C or (r == 0 and c == 5) or (r == 1 and c == 7) or (r == 4 and c == 0) or (r == 10 and c == 6)


def move_recursive(r: int, c: int):
    print(f'Moved to ({r}/{c})')
    if r == GRID_MAX_R and c == GRID_MAX_C:
        print(f'Target ({GRID_MAX_R}/{GRID_MAX_C}) reached')
        return

    if not is_off_limit(r, c + 1):
        move_recursive(r, c + 1)
        return

    if not is_off_limit(r + 1, c):
        move_recursive(r + 1, c)
        return

    print('Cannot reach target')


def move_iterative():
    x_moved = 0
    y_moved = 0
    for xi in range(x_moved, GRID_MAX_R + 1):
        x_moved = xi
        for yi in range(y_moved, GRID_MAX_C + 1):
            y_moved = yi
            print(f'Moved to ({xi}/{yi})')
            if not is_off_limit(xi, yi + 1):
                continue
            else:
                break
        if not is_off_limit(xi + 1, y_moved):
            continue
        else:
            break
    if x_moved == GRID_MAX_R and y_moved == GRID_MAX_C:
        print(f'Target ({GRID_MAX_R}/{GRID_MAX_C}) reached')
    else:
        print('Cannot reach target')


def calculate_recursive(r: int, c: int, steps: list[(int, int)], results: dict[(int, int), bool]) -> bool:
    if (r, c) in results:
        return results[(r, c)]

    result = False
    if is_off_limit(r, c):
        result = False
    elif (r == GRID_MAX_R and c == GRID_MAX_C) or calculate_recursive(r + 1, c, steps, results) or calculate_recursive(r, c + 1, steps, results):
        steps.append((r, c))
        result = True

    results[(r, c)] = result

    return result


# move_recursive(0, 0)
# move_iterative()
steps = []
target_reached = calculate_recursive(0, 0, steps, {})
if target_reached:
    print('Target reached!')
steps.reverse()
for step_r, step_c in steps:
    print(f'({step_r}/{step_c})')
