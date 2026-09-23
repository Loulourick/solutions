def circle_diameter(radius):
    diameter = radius * 2
    return diameter
def sum_range(start, end):
    otv = 0
    for i in range(start, end + 1):
        otv += i
    return otv
print (circle_diameter(5))
print(sum_range(100, 500))
print(sum_range(1, 10))
print(sum_range(500, 500))