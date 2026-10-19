def insertion_sort(arr):
    res = arr
    for i in range(len(res)):
        h = i
        while h > 0 and res[h - 1] > res[h]:
            res[h - 1], res[h] = res[h], res[h - 1]
            h -= 1
    return res
if __name__ == "__main__":
    insertion_sort([4, 2, 7, 1, 3, 5])  # [1, 2, 3, 4, 5, 7]
    insertion_sort([7, 3, 3, 4, 1])  # [1, 3, 3, 4, 7]
    insertion_sort([])  # []