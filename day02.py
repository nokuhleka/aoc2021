import numpy as np
import io as io
data = open('./data/day02.txt').readlines()

# Opdracht 1
directions = {'up':(0,-1), 'down':(0,1),'forward':(1,0)}
x,y = 0,0
for line in data: 
    operation, value = line.split()
    value = int(value)
    dx,dy = directions[operation]
    x += dx*value
    y += dy*value
    
print(x*y)

# Opdracht 2
directions = {'up':(0,-1), 'down':(0,1),'forward':(1,0)}
x,y,aim = 0,0,0
for line in data: 
    operation, value = line.split()
    value = int(value)
    dx,daim = directions[operation]
    x += dx*value
    aim += daim*value
    y += dx*value*aim
    
print(x*y)