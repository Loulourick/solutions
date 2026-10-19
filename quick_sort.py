def quick_sort(arr):
    if len(arr) <= 1: return arr
    char = arr[len(arr) // 2]
    left = []
    mid = []
    right = []
    for i in arr:
        if i < char: left.append(i)
        if i == char: mid.append(i)
        if i > char: right.append(i)
    return quick_sort(left) + mid + quick_sort(right)
if __name__ == "__main__":
    quick_sort([4, 2, 7, 1, 3, 5])   # [1, 2, 3, 4, 5, 7]
    quick_sort([7, 3, 3, 4, 1])      # [1, 3, 3, 4, 7]
    quick_sort([])                   # []