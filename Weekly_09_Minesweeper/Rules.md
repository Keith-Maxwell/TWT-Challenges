# Minesweeper challenge

[Discord Challenge message](https://discordapp.com/channels/501090983539245061/680851798340272141/734811056215687318)

Continued from the matrix challenge: The building's haunted rooms are supposed to be the only ones that are potentially haunted. But as time goes on the Tech With Tim staff started to become suspicious of more and more places in the building. So they decided to buy some land for the construction of a new office.

A trusted friend happened to come by, and while catching up with each other, the friend told the staff team that he'd heard of the land they bought to have mines planted and never taken out since WWII. The team decides to hire you, a well known mine expert, to dispose of the mines. Before you can dispose of the mines however you first need to find them.

## Task

Given a 2d matrix, return the same matrix but with each element having a number indicating how many mines total are adjacent to it vertically, horizontally, or diagonally. Mines being represented by an "x"

### example

```python
>>> print(solution([[ 0 , 0 , 0 ,'x', 0 ],
                    ['x', 0 , 0 ,'x', 0 ],
                    [ 0 , 0 , 0 , 0 , 0 ]]))
[[ 1 , 1 , 2 ,'x', 2 ],
 ['x', 1 , 2 ,'x', 2 ],
 [ 1 , 1 , 1 , 1 , 1 ]]
```

## Submission and grading criteria

- function name must be solution
- function must return the result
- no libraries/imports
- submit using the discord code block (type "t.tag discord code" without the quotes in #bot-commands for more info)
