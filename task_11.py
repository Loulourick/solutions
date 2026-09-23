def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n
    for k, seat in enumerate(seats):
        guest_number = k + 1
        result[seat - 1] = guest_number
    return result
print (guests_by_seat([1, 2, 3, 5, 4]))
print (guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5]))