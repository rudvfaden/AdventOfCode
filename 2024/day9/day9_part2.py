

data = '2333133121414131402'  # read_aoc_data()


unpacked_data = []
block = 0
for idx, value in enumerate(data.strip()):
    if idx % 2 == 0:
        unpacked_data.append([block] * int(value))
        block += 1
    elif int(value) != 0:
        unpacked_data.append([None] * int(value))

print(unpacked_data)


def first_none_index(lst: list) -> int:
    for idx, value in enumerate(lst):
        if value is None:
            return idx


def find_first_none_sublist(arr):
    for idx, sublist in enumerate(arr):
        if all(item is None for item in sublist):
            return idx, sublist
    return None


print(find_first_none_sublist(unpacked_data))


for i, list in enumerate(unpacked_data):
    # tjekker om subliste er none
    new_sublist = []
    new_none_list = []
    none_idx = 0
    if first_none_index(list) is not None:
        # finder længden på tomme subliste
        first_none_sublist_idx, sublist = find_first_none_sublist(
            unpacked_data)
        first_none_length = len(sublist)
        if first_none_length >= len(unpacked_data[-1]):
            last_value = unpacked_data.pop()
            last_value_lenght = len(last_value)
            for j in range(first_none_length):
                if j < last_value_lenght and last_value[j] is not None:
                    new_sublist.extend([last_value[j]])
                else:
                    new_none_list.extend([None])
                    none_idx += 1
            if None in list and len(unpacked_data) > i:
                unpacked_data[i] = new_sublist
                unpacked_data.insert(i+1, new_none_list)

print(unpacked_data)
