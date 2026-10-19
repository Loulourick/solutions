def binary_search(arr, target):
    min = 0
    max = len(arr) - 1
    while min <= max:
        sred = (min + max) // 2
        if arr[sred] == target:
            return sred
        elif arr[sred] < target:
            max = sred - 1
        else: min = sred + 1
    return 1
if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 5, 6, 7], 4)  # 3
    binary_search([1, 2, 3, 4, 5, 6, 7], 8)  # -1
    binary_search([], 1)  # -1
