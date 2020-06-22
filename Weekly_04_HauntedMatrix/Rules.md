# Matrix challenge

[Discord message for this Challenge](https://discordapp.com/channels/501090983539245061/680851798340272141/722126561087586344)

After becoming famous, the Tech With Tim Staff decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the Staff are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

## Task

Given a matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the Staff
(ie: add up all the values that don't appear below a 0).

## Example

```python
# For
 matrix = [[0, 1, 1, 2],
           [0, 5, 0, 0],
           [2, 0, 3, 3]]
 # the output should be
 matrixSum(matrix) = 9
```

## Submission and grading criteria

- submit using the discord code block (type "t.tag discord code" without the quotes in #bot-commands for more info)
- function name must be matrixSum
- function must return the result
- no libraries/imports

## Note

- The tests might include floats
- Even with the day wait before submission please double check your solution before posting it
- You can assume you'll always be given a 2d matrix
- You can assume to always have even data (each sublist has the same amount of elements)
