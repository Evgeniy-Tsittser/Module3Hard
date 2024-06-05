data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(args):
    summ_ = 0
    for i in args:
        if isinstance(i, list | tuple | set):
            summ_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key in i:
                if isinstance(key, str):
                    summ_ += len(key)
                elif isinstance(key, int | float):
                    summ_ += key
            for j in i.values():
                if isinstance(j, str):
                    summ_ += len(j)
                elif isinstance(j, int | float):
                    summ_ += j
        elif isinstance(i, int | float):
            summ_ += i
        elif isinstance(i, str):
            summ_ += len(i)

    return summ_


result = calculate_structure_sum(data_structure)
print(result)
