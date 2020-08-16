from random import randint
from timeit import timeit


def checker(value1, weight1, value2, weight2, maxW):  # the official solution, clever and beautiful
    return max(value1*(weight1 <= maxW),
               value2*(weight2 <= maxW),
               (value1+value2)*(weight1+weight2 <= maxW))


def solution(value1, weight1, value2, weight2, maxW):  # My solution, ugly and did not work
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


def gen():
    def s(): return randint(0, 20)
    return s(), s(), s(), s(), s()


def batch_tester():
    n_test = 2000
    passed = 0
    for _ in range(n_test):
        if solution(*gen()) == checker(*gen()):
            passed += 1
    print(f'passed cases : {passed}')
    print(f'failed cases: {n_test - passed}')


batch_tester()
