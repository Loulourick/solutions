def compare(m, n):
    if m > n: return "Number m > n"
    if m < n: return "Number m < n"
    if m == n: return "The numbers are equal"
if __name__ == "__main__":
    print(compare(5, 3))
    print(compare(3, 5))
    print(compare(4, 4))
