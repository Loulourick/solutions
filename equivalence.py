from itertools import *
def are_equivalent(f, g, n):
    for arguments in product([False, True], repeat  = n):
        if (f(*arguments)) != (g(*arguments)): return False
    return True
def de_morgan_left(a, b):
    return not (a and b)

def de_morgan_right(a, b):
    return (not a) or (not b)

def wrong(a, b):
    return (not a) and (not b)
def de_morgan_and_left(a, b):
    return not (a and b)


def de_morgan_and_right(a, b):
    return (not a) or (not b)


def de_morgan_or_left(a, b):
    return not (a or b)


def de_morgan_or_right(a, b):
    return (not a) and (not b)


def implies(a, b):
    return (not a) or b
if __name__ == "__main__":
    are_equivalent(de_morgan_left, de_morgan_right, 2)   # True
    are_equivalent(de_morgan_left, wrong, 2)             # False