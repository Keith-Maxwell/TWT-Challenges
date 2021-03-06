# Theater escape challenge

[Discord message](https://discordapp.com/channels/501090983539245061/680851798340272141/727180475256406156)

Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since you have two exits conveniently situated both to your right and your left. Make your way to the exit.

The main problem is your shyness: you're afraid that you'll end up disturbing (even if only for a couple of seconds) the people you'll be passing by. To gain some courage, you decide to calculate the number of such people and see which exit you can get to with disturbing the least amount of people.

## Task

You are given a 2d matrix with values that indicate where there are people sitting, where you are, and empty seats

<u>Example</u>

```python
[[1, 1, 1, 1, 1],
[-1, 1, -1, 1, 1],
[1, 0, -1, 1, 1]]
```

no one there: -1
person sitting: 1
you: 0

return "left" or "right" depending on which way to go to disturb the least amount of people.\
In this case it will be "left". (choose left or right from the perspective of looking at it from the top or the way you are looking at the matrix)

## Submission and Grading

- the function is called `whichExit`
- the function needs to return a string that either contains left or right
- please use the discord block for submitting (use "t.tag discord code" in #bot-commands for more info)

If there are the same amount of people on both sides return "same"

No edge cases on this one (none that I can think off anyway)
