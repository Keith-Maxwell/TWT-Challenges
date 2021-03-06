# Treasure challenge

[Discord Challenge message](https://discordapp.com/channels/501090983539245061/680851798340272141/742433523369246840)

It's a lovely day, you're once again visiting the Tech With Tim Building. Suddenly, as you walk down the stairs, you find a special treasure chest! There are two items in it!

## Task

The first item weighs `weight1` and is worth `value1`, and the second item weighs `weight2` and is worth `value2`. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is `maxW` and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

### example

```python
>>> value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, maxW = 8
>>> solution(value1, weight1, value2, weight2, maxW)
10
```

You can only carry the first item.

```python
>>> value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, maxW = 9
>>> solution(value1, weight1, value2, weight2, maxW)
16.
```

You're strong enough to take both of the items with you.

## Submission and grading

- code must be in a function
- function must be named/called solution
- function must accept 5 integers as arguments
- function must return an integer
- no libraries/imports allowed
