def is_divisor(a, b):
    if a == 0: return False
    return b % a == 0
print (is_divisor(3, 12))
print (is_divisor(5, 12))
print (is_divisor(0, 12))
print (is_divisor(7, 0))