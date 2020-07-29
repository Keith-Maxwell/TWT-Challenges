# Day challenge

[Discord Challenge message](https://discordapp.com/channels/501090983539245061/680851798340272141/737479056974544937)

It's the 20th March, you're filling out some paperwork and when you get to where it usually asks you to fill in the date instead it's asking you for the day of the week. Problem is you only remember that the 15th March was a Thursday.

## Task

Given the day of the week, its date, and a second date, return the day of the week that corresponds with the second number of the month given (month numbers and the week days do not and will not match with reality)

### example

```python
>>> print(solution("Tuesday", "13/04", "15/04"))
Thursday
```

## Note

You can assume all months have 30 days.
You can assume there is only one year that exists meaning if you get a date like 23/12 and need to search for 03/01 you go backwards to find it not forward.

## Submission and grading

- function name must be solution
- function must take three arguments
- function must return a string
- dates will always be given in DD/MM format
- letter case should not matter (your function should be able to handle "Monday" and "moNdaY" the same)
- no imports/libraries allowed
