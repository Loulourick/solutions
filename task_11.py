def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n
    k = 1
    for i in seats:
        result[i-1] = k
        k +=1
    return result
if __name__ == "__main__":
    guests_by_seat([1, 2, 3, 5, 4])
    guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5])
