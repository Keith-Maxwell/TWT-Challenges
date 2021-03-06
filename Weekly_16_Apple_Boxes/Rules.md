# Apple Boxes

You have `k` apple boxes full of apples. Each square box of size `m` contains `m × m` apples. You just noticed two interesting properties about the boxes:

1. The smallest box is size 1, the next one is size 2,..., all the way up to size `k`.

2. Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
   ‍

## Task

Your task is to calculate the difference between the number of red apples and the number of yellow apples.

### Examples

For k = 5, the output should be

```python
>>> print(solution(5))
-15.
```

There are `1 + 3 * 3 + 5 * 5 = 35` yellow apples and `2 * 2 + 4 * 4 = 20` red apples, making the answer `20 - 35 = -15`.

## Submission and grading

- code must be written in python
- code must be in a function
- function must be named solution
- function must take a integer (k) as an argument
- function must return a integer
- no imports/libraries allowed
