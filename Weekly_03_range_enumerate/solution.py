import random


def erange(*args):
    ''' recreation of the range() function\n
        erange(stop) -> from 0 to stop value with step 1\n
        erange(start, stop) -> from start to stop, with step 1\n
        erange(start, stop, step) -> from start to stop, with given step'''
    for arg in args:  # verify that every argument is an integer
        if type(arg) != int:
            raise TypeError("arguments must be integers")

    if len(args) == 1:  # one argument, goes from 0 to arg
        if args[0] <= 0:
            return []
        i, lst = 0, []
        while i != args[0]:
            lst.append(i)
            i += 1

    elif len(args) == 2:  # two arguments, start and stop
        if args[1] <= args[0]:
            return []
        i, lst = args[0], []
        while i < args[1]:
            lst.append(i)
            i += 1

    elif len(args) == 3:  # 3 arguments, start, stop, step
        if (args[1] >= args[0] and args[2] < 0) or (args[1] <= args[0] and args[2] > 0):
            return []
        i, lst = args[0], []
        if args[2] < 0:  # negative step
            while i > args[1]:
                lst.append(i)
                i += args[2]
        elif args[2] > 0:  # positive step
            while i < args[1]:
                lst.append(i)
                i += args[2]
        elif args[2] == 0:
            raise ValueError("range() arg 3 must not be 0")

    else:  # no arguments or more than 3 arguments raises an error
        raise SyntaxError("one, two or three arguments supported, no more, no less")

    return lst


def numerate(iterable, start=0):
    ''' recreation of the enumerate() function'''
    if type(start) != int:
        raise TypeError('start should be of type int')
    index = 0 + start
    for element in iterable:
        yield(index, element)
        index += 1


# --------------------------------TESTS---------------------------------------
# Test the erange() function
psp = 0
psn = 0
for x in range(21):
    for y in range(21):
        for z in range(21):
            if z - 10 != 0:
                try:
                    if erange(x-10, y-10, z-10) == list(range(x-10, y-10, z-10)):
                        psp += 1
                    else:
                        psn += 1
                except:
                    print(x-10, y-10, z-10)
print(f'successes : {psp}, failures : {psn}')
if psn == 0:
    print("Success ! erange() is the same as range()")
else:
    print("Failed ! Try again...")

# test the numerate function
choices = (True, False)
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
# if nothing prints in the console, then everything works fine
