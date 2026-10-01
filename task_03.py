def is_divisor(a, b):
    if a == 0: return False
    return b % a == 0
if __name__ == "__main__":
    is_divisor(3, 12)
    is_divisor(5, 12)
    is_divisor(0, 12)
    is_divisor(7, 0)
