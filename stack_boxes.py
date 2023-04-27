import functools


def can_be_stacked(box: tuple[int, int, int], stacked: list[tuple[int, int, int]]):
    if len(stacked) == 0:
        return True
    all_stacked_lengths_greater = all(b[0] >= box[0] for b in stacked)
    all_stacked_widths_greater = all(b[1] >= box[1] for b in stacked)
    all_stacked_heights_greater = all(b[2] >= box[2] for b in stacked)
    return all_stacked_lengths_greater and all_stacked_widths_greater and all_stacked_heights_greater


def stack_boxes_recursive(remaining: list[tuple[int, int, int]], stacked: list[tuple[int, int, int]], result: list[tuple[int, list[tuple[int, int, int]]]]):
    if len(remaining) == 0:
        result.append((get_height(stacked), stacked))
        return
    is_end = True
    for r in remaining:
        stacked_new = [] if len(stacked) == 0 else stacked
        if can_be_stacked(r, stacked_new):
            is_end = False
            remaining_copy = remaining.copy()
            remaining_copy.remove(r)
            stacked_new.append(r)
            stack_boxes_recursive(remaining_copy, stacked_new, result)
    if is_end:
        result.append((get_height(stacked), stacked))


def get_height(stacked):
    return functools.reduce(lambda x, y: x + y, [x[2] for x in stacked], 0)


boxes = [(100, 100, 100), (400, 400, 400), (200, 200, 200), (300, 300, 300)]
result = []
stack_boxes_recursive(boxes, [], result)
print(result)
result.sort(key=lambda x: x[0], reverse=True)
print(result[0][0])
