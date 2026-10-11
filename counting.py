# import math
# def factorial(n):
#     if n < 0: return None
#     return math.factorial(n)
#
# def arrangements(n, k):
#     if k > n or k < 0 or n < 0: return 0
#     return math.factorial(n) // math.factorial(n - k)
#
# def combinations(n, k):
#     if k > n or k < 0 or n < 0: return 0
#     return math.comb(n,k)
def factorial(n):
    if n < 0: return 0
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k
def arrangements(n, k):
    if k > n or k < 0 or n < 0: return 0
    g = 1
    for i in range(n - k + 1, n + 1):
        g *= i
    return g
def combinations(n, k):
    if k > n or k < 0 or n < 0: return 0
    return arrangements(n, k)// factorial(k)
if __name__ == "__main__":
    factorial(0)          # 1
    factorial(5)          # 120
    factorial(-1)         # None

    arrangements(13, 6)   # 1235520
    arrangements(4, 2)    # 12
    arrangements(5, 5)    # 120
    arrangements(3, 5)    # 0

    combinations(13, 6)   # 1716
    combinations(4, 2)    # 6
    combinations(64, 8)   # 4426165368
    combinations(5, 0)    # 1