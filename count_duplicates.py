def count_duplicates(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return sum(1 for amount in counts.values() if amount > 1)


if __name__ == "__main__":
    count_duplicates("abcde")  # 0
    count_duplicates("aabbcde")  # 2    a и b
    count_duplicates("aabBcde")  # 2    a и b, регистр не важен
    count_duplicates("indivisibility")  # 1    i встречается шесть раз
    count_duplicates("aA11")  # 2    a и 1
