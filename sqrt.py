def integer_square_root(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid + 1
        else:
            right = mid - 1
    return right
if __name__ == "__main__":
    integer_square_root(0)  # 0
    integer_square_root(4)  # 2
    integer_square_root(8)  # 2
    integer_square_root(10)  # 3
    integer_square_root(100)  # 10
    integer_square_root(10 ** 12)  # 1000000
