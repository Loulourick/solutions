def duplicate_encode(text):
    norm = text.lower()
    counts = {}

    for char in norm:
        counts[char] = counts.get(char, 0) + 1

    return "".join("(" if counts[char] == 1 else ")" for char in norm)


if __name__ == "__main__":
    duplicate_encode("din")  # "((("
    duplicate_encode("recede")  # "()()()"
    duplicate_encode("Success")  # ")())())"
    duplicate_encode("(( @")  # "))(("