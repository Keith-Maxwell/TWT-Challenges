def whichExit(matrix):
    for row in matrix:
        if 0 in row:
            left_people, right_people = 0, 0
            for seat in range(len(row)):
                if row[seat] == 1 and seat < row.index(0):
                    left_people += 1
                if row[seat] == 1 and seat > row.index(0):
                    right_people += 1
            return("left" if left_people < right_people else "right" if right_people < left_people else "same")


if __name__ == "__main__":

    m = [[1, 1, 1, 1, 1],
         [-1, 1, -1, 1, 1],
         [1, 0, -1, 1, 1]]
    print(whichExit(m))  # should print "left"

    m = [[1, 1, 1, 1, 1],
         [-1, 1, -1, 1, 1],
         [1, 0, -1, -1, 1]]
    print(whichExit(m))  # should print "same"

    m = [[1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, 0, 1],
         [1, -1, -1, -1, 1, 1]]
    print(whichExit(m))  # should print "right"

    import time as t
    start = t.time()
    for _ in range(100000):
        _ = whichExit(m)  # should print "left"
    stop = t.time()
    print(f'Total time = {(stop - start)/100000} seconds per matrix')
