from itertools import *
def truth_table(n):
    if n == 0: return [()]
    return list(product((0,1), repeat = n))
if __name__ == "__main__":
    truth_table(1)
    truth_table(2)
    truth_table(3)
    truth_table(0)