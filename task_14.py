def circle_diameter(radius):
    diameter = radius * 2
    return diameter
def sum_range(start, end):
    otv = 0
    for i in range(start, end + 1):
        otv += i
    return otv
if __name__ == "__main__":
    circle_diameter(5)
    sum_range(100, 500)
    sum_range(1, 10)
    sum_range(500, 500)
