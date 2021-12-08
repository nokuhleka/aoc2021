import numpy as np
data = np.loadtxt('./data/day01', dtype=int)
print(data)

# Opdracht 1
ans1 = data[1:]-data[:-1]
print(sum(ans1 > 0))

# Opdracht 2
ansb = data[0:-2]+data[1:-1]+data[2:]
ans2 = ansb[1:]-ansb[:-1]
print(sum(ans2 > 0))