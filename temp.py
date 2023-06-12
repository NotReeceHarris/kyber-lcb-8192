import numpy as np


key = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

content = np.array([
    [19, 15, 13, 17, 3],
    [7, 11, 8, 4, 24],
    [4, 0, 18, 0, 26]
])

print(np.dot(key, content).tolist())

print(np.linalg.inv(key))