otv = []
def multiplication_table(n):
    for i in range(1, 11):
        otv.append(f"{n} x {i} = {n * i}")
    return otv
print(multiplication_table(7))
