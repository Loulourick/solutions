def insertion_sort(arr):
    res = arr.copy()
    for i in range(1, len(res)):
        cor = res[i]
        h = i
        while h > 0 and res[h - 1] > cor:
            res[h] = res[h - 1]
            h -= 1

        res[h] = cor
        
    return res
if __name__ == "__main__":
    insertion_sort([4, 2, 7, 1, 3, 5])  # [1, 2, 3, 4, 5, 7]
    insertion_sort([7, 3, 3, 4, 1])  # [1, 3, 3, 4, 7]
    insertion_sort([])  # []
