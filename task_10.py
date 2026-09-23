def index_of_min(values):
    if not values: return -1
    min_value = min(values)
    return values.index(min_value)

print(index_of_min([10, -3, -5, 2, 5]))
print(index_of_min([1, 2, 3]))
print(index_of_min([4, 1, 1, 9]))
print(index_of_min([]))