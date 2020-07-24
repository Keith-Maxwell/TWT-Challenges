def solution(grid):
    HEIGHT, WIDTH = len(grid), len(grid[0])
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] != 'x':
                neighbors = [(row+i, col+j) for i in range(-1, 2) for j in range(-1, 2)]
                for n in neighbors:
                    if -1 < n[0] < HEIGHT and -1 < n[1] < WIDTH:
                        if grid[n[0]][n[1]] == 'x':
                            grid[row][col] += 1

    return grid


if __name__ == "__main__":
    print(solution([[0, 0, 0, 'x', 0],
                    ['x', 0, 0, 'x', 0],
                    [0, 0, 0, 0, 0]]))
