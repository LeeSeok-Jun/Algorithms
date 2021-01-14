"""
2차원 배열 회전 알고리즘
- 시계방향으로 90도 회전하는 알고리즘
"""

array = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
n = len(array)

rotated_array = [[0] * n for _ in range(n) ]

for i in range(n):
    for j in range(n):
        rotated_array[j][n-1-i] = array[i][j]

print(rotated_array)