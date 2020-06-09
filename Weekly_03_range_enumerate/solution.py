def erange(*args):
    ''' recreation of the range() function\n
        erange(stop) -> from 0 to stop value with step 1\n
        erange(start, stop) -> from start to stop, with step 1\n
        erange(start, stop, step) -> from start to stop, with given step'''

    if len(args) == 0 or len(args) > 3:
        raise TypeError("one, two or three arguments supported, no more, no less")

    if any([type(i) != int for i in args]):
        raise TypeError("arguments must be integers")

    start = args[0] if len(args) >= 2 else 0
    stop = args[1] if len(args) >= 2 else args[0]
    step = args[2] if len(args) == 3 else 1

    if step == 0:
        raise ValueError("Step should not be 0, user is stoopid here")

    i = start
    while (i > stop) if step < 0 else (i < stop):
        yield i
        i += step


def numerate(iterable, start=0):
    ''' recreation of the enumerate() function'''
    if type(start) != int:
        raise TypeError('start should be of type int')
    index = 0 + start
    for element in iterable:
        yield(index, element)
        index += 1


if __name__ == "__main__":

    # --------------------------------TESTS---------------------------------------
    # Test the erange() function
    psp = 0
    psn = 0
    for x in range(21):
        for y in range(21):
            for z in range(21):
                if z - 10 != 0:
                    try:
                        if list(erange(x-10, y-10, z-10)) == list(range(x-10, y-10, z-10)):
                            psp += 1
                        else:
                            psn += 1
                    except:
                        psn += 1
                        print(x-10, y-10, z-10)
    print(f'successes : {psp}, failures : {psn}')
    if psn == 0:
        print("Success ! erange() is the same as range()")
    else:
        print("Failed ! Try again...")

    # test the numerate function
    import random
    choices = (True, False)
    flag = False
    for _ in range(1000):
        iter = list(range(random.randint(1, 50), random.randint(50, 100)))
        choice = random.choice(choices)
        if choice:
            test = list(numerate(iter.copy()))
            valid = list(enumerate(iter))
        else:
            strt = random.randint(-100, 100)
            test = list(numerate(iter.copy(), start=strt))
            valid = list(enumerate(iter, start=strt))
        if test != valid:
            print('failed:')
            print(f'Yours: {test}')
            print(f'Correct: {valid}')
            flag = True
    if not flag:
        print("Success ! The numerate() function is the same as enumerate()")
    # if nothing prints in the console, then everything works fine
