import math


def gather_subsets_recursive(the_set: frozenset, set_sum: dict[frozenset, bool]):
    if the_set in set_sum:
        return

    set_sum[the_set] = True
    for s in the_set:
        removed = set(the_set)
        removed.remove(s)
        gather_subsets_recursive(frozenset(removed), set_sum)


def gather_subsets_iterative1(the_set: []) -> list[set]:
    set_sum = [{}]
    length = len(the_set)
    for i in range(int(math.pow(2, length))):
        sub_set = set()
        for j in range(length):
            bit_mask = 1 << j
            if bit_mask & i > 0:
                sub_set.add(the_set[j])
        if len(sub_set) > 0:
            set_sum.append(sub_set)
    return set_sum


def gather_subsets_iterative2(the_set: set) -> []:
    set_sum = [{}]
    for x in the_set:
        to_be_added = []
        for s in set_sum:
            copy = set(s.copy())
            copy.add(x)
            to_be_added.append(copy)
        for a in to_be_added:
            set_sum.append(a)
    return set_sum


the_set = frozenset({'a', 'b', 'c', 'd'})
set_sum = dict()
gather_subsets_recursive(the_set, set_sum)
print(set_sum.keys())
print(len(set_sum.keys()))

result_iterative1 = gather_subsets_iterative1(list(the_set))
print(result_iterative1)
print(len(result_iterative1))

result_iterative2 = gather_subsets_iterative2(set(the_set))
print(result_iterative2)
print(len(result_iterative2))