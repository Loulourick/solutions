def linear_search(arr, target):
    for i in range (len(arr) - 1):
        if arr[i] == target:
            return i
    return -1
if __name__ == "__main__":
    linear_search([5, 3, 7, 1, 4], 1)  # 3
    linear_search([5, 3, 7, 1, 4], 6)  # -1
    linear_search([1, 2, 2, 3], 2)  # 1   первое вхождение
    linear_search([], 1)  # -1