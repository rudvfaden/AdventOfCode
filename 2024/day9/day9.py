from read_aoc_data import read_aoc_data
import time
from tqdm import tqdm
import numpy as np

data = read_aoc_data()

# indlæs numpy array
values = np.array([int(x) for x in data.strip()])
# opdel i tomme og ikke tomme bloks
even_indices = np.arange(0, len(values), 2)
odd_indices = np.arange(1, len(values), 2)

# gentag blocks
blocks = np.repeat(np.arange(len(even_indices)), values[even_indices])

# lav tomme værdier bruger -1
none_blocks = np.repeat(-1, np.sum(values[odd_indices]))

# Combine the arrays
unpacked_data = []
even_start = 0
odd_start = 0
# samler data
for i in range(len(values)):
    if i % 2 == 0:
        count = values[i]
        unpacked_data.extend(blocks[even_start:even_start + count])
        even_start += count
    else:
        count = values[i]
        unpacked_data.extend(none_blocks[odd_start:odd_start + count])
        odd_start += count

unpacked_data = np.array(unpacked_data)

start_time = time.time()

for _ in tqdm(range(len(unpacked_data))):
    # tjekker om der er tomme værdier (-1)
    none_indices = np.where(unpacked_data == -1)[0]
    if len(none_indices) > 0:
        first_none = none_indices[0]
        last_value = unpacked_data[-1]
        unpacked_data = unpacked_data[:-1]  # fjern sidste værdi
        if first_none < len(unpacked_data):
            unpacked_data[first_none] = last_value
    else:
        break

# finder index af blocks
indices = np.arange(len(unpacked_data))
# bruger numpy's array multiplikation
resultat = np.sum(indices * unpacked_data)
print(resultat)

end_time = time.time()
print(f"Execution time: {end_time - start_time:.6f} seconds")

