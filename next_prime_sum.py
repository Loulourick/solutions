def mn (n,p):
    result = 0
    while n >= p:
        n //= p
        result += n
    return result

def max_power(n, k):
    otvet = float("inf")
    d = 2
    while d * d <= k:
        l = 0
        while k % d == 0:
            k //= d
            l += 1
        if l > 0:
            res = mn(n,d)
            otvet = min(otvet,res // l)
        d += 1
    if k > 1:
        res = mn(n,k)
        otvet = min(otvet,res)
    return otvet
if __name__ == "__main__":
    max_power(10, 2)     # 8
    max_power(10, 3)     # 4
    max_power(10, 5)     # 2
    max_power(5, 2)      # 3
    max_power(10, 10)    # 2
    max_power(25, 6)     # 10
    max_power(100, 12)   # 48
    max_power(1000, 7)   # 164