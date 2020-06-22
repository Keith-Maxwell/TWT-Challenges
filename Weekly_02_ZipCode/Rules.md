# **Zip/Postal code validating challenge**

[Discord message for this Challenge](https://discordapp.com/channels/501090983539245061/680851798340272141/717049215452446802)

(please make sure to read everything so you know exactly what is expected, feel free to ask any questions you have)

## Task:

Check that a given postal code is valid, 3 things need to be checked:

- it's made of only integers
- there are 5 integers total, no less no more
- there are no repetitive or neighboring digits

That last check can be a bit confusing at first so let me try to explain it here: let's say that `x` can be any digit

```
11xxx # two or more same digits in a row, not valid
1x1xx # two or more neighboring digits, not valid
1xx1x # no neighboring or next to each other digits, valid
```

If you still have any questions about that last check please let me know

## Grading criteria:

- No libraries/imports allowed - The code needs to be within a function - Hav
- e the function named exactly `validate`
- Have the function take the code as an argument
- Have the function return True if the code is valid, and False otherwise (do not throw exceptions or print stuff if it's not valid, just return False)
- Obviously do all the checks

## Submission:

Have the code within a discord code: `py # your code` make sure you're using the tick marks ` not the quotes ' so on pc your code should look colorful

```
"for example a string like this should look greeny on pc"
```

## Note:

- I know this **does not reflect** how **real world postal codes** work. It was just a convenient naming for the challenge, any alternative challenge names are welcome.

- You can only submit your code once, so check, double check, and triple check your solution before posting ;)
