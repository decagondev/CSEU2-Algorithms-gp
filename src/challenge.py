# Work out the time complexity of these solutions

"""
Formally:
1. Compute the Big-O for each line in isolation
2. if something is in a loop, multiply it's Big-O by the loop for the total.
3. If two things happen sequentially, add the Big-Os.
4. Drop leading multiplicative constants from each of the Big-Os.
5. From all of the Big-Os that are added, drop all but the biggest, dominating one.
"""
import math
# 1
def baz(n):
    s = 0

    for i in range(n):
        for j in range(int(math.sqrt(n))):
            s += i * j
    
    return s

# 2
def frotz(n):
    s = 0

    for i in range(n):
        for j in range(2 * n):
            s += i * j

    return s

# 3
def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += sum
        for _ in range(0, x):
            for _ in range(x, x + 15):
                sum += 1