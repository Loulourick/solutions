def count_positives_sum_negatives(numbers):
    if not numbers:
        return []

    positive = 0
    negativesum = 0

    for number in numbers:
        if number > 0:
            positive += 1
        elif number < 0:
            negativesum += number

    return [positive, negativesum]


if __name__ == "__main__":
    count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
    # [10, -65]

    count_positives_sum_negatives([0, 0, 0])  # [0, 0]
    count_positives_sum_negatives([])  # []
