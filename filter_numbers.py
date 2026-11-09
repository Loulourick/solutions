def filter_numbers(items):
    return [item for item in items if isinstance(item, int) and not isinstance(item, bool)]


if __name__ == "__main__":
    filter_numbers([1, 2, "a", "b"])  # [1, 2]
    filter_numbers([1, "a", "b", 0, 15])  # [1, 0, 15]
    filter_numbers([1, 2, "aasf", "1", "123", 123])  # [1, 2, 123]