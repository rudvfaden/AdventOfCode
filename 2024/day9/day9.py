from read_aoc_data import read_aoc_data

data = read_aoc_data()

unpacked_data = []
block = 0
for idx, value in enumerate(data.strip()):
    if idx % 2 == 0:
        unpacked_data.extend([block] * int(value))
        block += 1
    else:
        unpacked_data.extend([None] * int(value))


def first_none_index(lst: list) -> int:
    for idx, value in enumerate(lst):
        if value is None:
            return idx


last_value = None
for idx, value in enumerate(unpacked_data):
    first_none = first_none_index(unpacked_data)
    if first_none:
        last_value = unpacked_data.pop()
        if first_none < len(unpacked_data):
            unpacked_data[first_none] = last_value
    else:
        break


resultat = sum(idx*block for idx, block in enumerate(unpacked_data))
print(resultat)
