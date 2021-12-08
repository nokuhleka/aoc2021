import numpy as np
import io as io

from numpy.lib.index_tricks import index_exp
data = open('./data/day03.txt').readlines()

str_lst = "1 2 3 4".split()
print("list of sting:", str_lst)

# Converteer een lijst dmv for-loop
int_lst = []
for s in str_lst:
    int_lst.append(int(s))

# Converteer een lijst met map functie
int_lst = map(int, str_lst)

# Converteer een lijst met een lijst-comprehensie
int_lst = [int(s) for s in str_lst]

def string_to_ints(s):
    return [int(ch) for ch in s.strip()]

def bits_to_int(s):
    """Converts sequence of bits into integer."""
    n = 0
    for bit in s:
        n = n*2 + bit
    return n

# def bits_to_int(s):
#     bit_str = "".join(str(i) for i in s)
#     return int(bit_str, 2)

# Opdracht 1
#gamma,epsilon
bits = np.array([string_to_ints(line) for line in data])
print(bits)

def ratings(bits):
    gamma = (bits.shape[0]/2 <= bits.sum(axis=0)).astype(int)
    epsilon = (bits.shape[0]/2 > bits.sum(axis=0)).astype(int)
    return gamma, epsilon

gamma, epsilon = ratings(bits)

print(bits_to_int(gamma) * bits_to_int(epsilon))

# zie je vaak, maar moet niet zo
lst = ["a", "b", "c"]
for i in range(len(lst)):
    print(f"lst[{i}] = {lst[i]}")

# maar zo
for i, a in enumerate(lst):
    print(f"lst[{i}] = {a}")

# Opdracht 2
def search_rating(bits, rating):
    for k in range(bits.shape[1]):
        if bits.shape[0] == 1:
            return bits[0]
        col = bits[:,k]
        r = ratings(col)[rating]
        idx = np.where(col == r)[0]
        bits = bits[idx]
    return bits[0]
    
oxygen = search_rating(bits, 0)
co2 = search_rating(bits, 1)
print(bits_to_int(oxygen)*bits_to_int(co2))
