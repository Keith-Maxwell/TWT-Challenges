from random import randint
from timeit import timeit


def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    elif weight2 <= maxW and weight1 > maxW:
        return value2
    elif weight2 > maxW and weight1 <= maxW:
        return value1
    return 0


# tests ---------------------------
value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 8
print(solution(value1, weight1, value2, weight2, maxW))  # 10
value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 9
print(solution(value1, weight1, value2, weight2, maxW))  # 16
value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 3
print(solution(value1, weight1, value2, weight2, maxW))  # 0
value1 = 10
weight1 = 5
value2 = 6
weight2 = 8
maxW = 7
print(solution(value1, weight1, value2, weight2, maxW))  # 10

# efficiency tester -----------------------------


def gen():
    def s(): return randint(0, 20)
    return s(), s(), s(), s(), s()


def tester(): solution(*gen())


print(timeit(tester))
