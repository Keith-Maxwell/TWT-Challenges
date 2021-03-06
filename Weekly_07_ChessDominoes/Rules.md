# Dominos and chess challenge

[Original Discord message](https://discordapp.com/channels/501090983539245061/680851798340272141/729712703999836271)

It can be fun to experiment using something in a way we don't usually use. Here we'll need to see whether or not we can completely fill up a chessboard with dominos having two spots or squares on the board unavailable to us

## Task

Given that 0's indicate open spots and 1's indicate unavailable or filled spots. Return True if a chessboard can be completely filled up with dominos, return False otherwise.

- the chessboard can be of any dimensions with all rows being the same length and all columns being the same length
- there will a random amount of spots filled up
- the dominos always take up two spots/squares either vertically or horizontally

### example

```python
>>> print(fill([[0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,0]]))
False
```

## Submission and grading

- function name must be fill
- function must only return either True or False
- no libraries/imports allowed in the submitted code
- please use the discord code block when submitting (type "t.tag discord code" without the quotes in #bot-commands for more info)

Have fun!
