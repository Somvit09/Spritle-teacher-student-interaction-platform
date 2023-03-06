from num2words import num2words
from word2number import w2n


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def divided_by(a, b):
    return a // b


def times(a, b):
    return a * b


def calculate_mathematical_operations(input_string):
    a = input_string.split('(')
    n1 = w2n.word_to_num(a[0])
    n2 = w2n.word_to_num(a[2])
    operation = a[1]
    if operation == 'plus':
        return plus(n1, n2)
    if operation == 'minus':
        return minus(n1, n2)
    if operation == 'times':
        return times(n1, n2)
    if operation == 'divided_by':
        return divided_by(n1, n2)


input_string = 'eight(minus(three()))'
print(calculate_mathematical_operations(input_string))