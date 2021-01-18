"""
파이썬 조합, 순열
"""

"""
조합
"""
from itertools import combinations

data = [1, 2, 3, 4, 5]

# 5C2
print(list(combinations(data, 2)))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

# 5C3
print(list(combinations(data, 3)))
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

"""
순열
"""
from itertools import permutations

# 5P2
print(list(permutations(data, 2)))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

# 5P4
print(list(permutations(data, 4)))