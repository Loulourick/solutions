import random
def quick_sort(arr):
    if len(arr) <= 1: return arr
    if len(arr) < 2: return sorted(arr)
    s = random.randint(0, len(arr) - 1)
    sup = arr[s]
    
    l = []
    e = []
    g = []

    for element in arr:
        if element < sup:
            l.append(element)
        elif element > sup:
            g.append(element)
        else:
            e.append(element)
    return quick_sort(l) + e + quick_sort(g)

if __name__ == "__main__":
    quick_sort([4, 2, 7, 1, 3, 5])  # [1, 2, 3, 4, 5, 7]
    quick_sort([7, 3, 3, 4, 1])  # [1, 3, 3, 4, 7]
    quick_sort([])  # []
