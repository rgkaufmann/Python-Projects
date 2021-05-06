import numpy as np


def ndm(n, m):
    return np.random.randint(1, m+1, n)


def charactercreation():
    scores = []
    for i in range(6):
        rolls = ndm(4, 6)
        scores.append(sum(rolls)-min(rolls))

    return scores
