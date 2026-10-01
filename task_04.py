def swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b
if __name__ == "__main__":
    print(swap(2,8))
# def swap(a,b):
#     a = a * b
#     b = a / b
#     a = a / b 
#     return a,b
# print(swap(4,16))
