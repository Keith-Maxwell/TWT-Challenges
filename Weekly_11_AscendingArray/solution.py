def solution(arr):
    counter = 0
    for i in range(len(arr)-1):
        while arr[i+1] <= arr[i]:
            arr[i+1] += 1
            counter += 1
    return counter


print(solution([1, 1, 1]))
print(solution([-1000, 0, -2, 0]))
print(solution([0]))
