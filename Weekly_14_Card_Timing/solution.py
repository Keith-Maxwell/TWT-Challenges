import timeit


# def solution(n_days):
#    return [28, 30, 31] if n_days == 31 else [31]

# short solution
solution=lambda n:n%2*[28,30]+[31]


def tester():
    a = {28: [31], 30: [31], 31: [28, 30, 31]}
    for x in [28, 30, 31]:
        if solution(x) != a[x]:
            raise Exception(f"Nope, your solution isn't correct (failed with {x})")
    print("Success")


tester()
