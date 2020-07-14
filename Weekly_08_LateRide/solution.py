

def lateRide(n):
    h = n // 60
    m = n % 60
    return(sum([int(x) for x in str(h)+str(m)]))


if __name__ == "__main__":
    import json
    import os
    with open(os.path.join('Weekly_08_LateRide', 'expectedResults.json')) as f:
        expectedResults = json.load(f)
    failed, success = 0, 0
    for testNumber in range(1440):
        if expectedResults[testNumber] != lateRide(testNumber):
            failed += 1
        else:
            success += 1
    print(f'Successful cases : \t{success}\nFailed cases : \t\t{failed}')
