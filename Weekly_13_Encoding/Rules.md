# Huffman encoding challenge

[Original Discord Message](https://discordapp.com/channels/501090983539245061/680851798340272141/744966934793158666)

You are one of Tims employees and as one of his favorite employees he gave you a challenging task. You need to come up with an encoding algorithm that encodes text in such a way that one would need a key to decode it.

## Task

Given a text, return an encoded version where each word is replaced by a number indicating its frequency in the text, 1 being the most used word, and the highest number being the least used word.

### example

```py
>>> print(solution('hi hi bye hi cya bye'))
1 1 2 1 3 2
```

## Submission and grading

- code must be written in python
- code must be in a function
- function name must be solution
- function must take in a string argument
- function must return a string
- no imports/libraries allowed

## Note

You can assume that:

- there will not be any new line characters
- there will not be any punctuation
