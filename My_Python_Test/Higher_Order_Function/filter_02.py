import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


newlist = filter(is_sqr, range(1, 101))
print(list(newlist))
