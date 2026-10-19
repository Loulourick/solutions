def is_anagram(s1, s2):
    first = len(s1)
    second = len(s2)
    if first != second: return False
    if sorted(s1) != sorted(s2): return False
    else: return True
if __name__ == "__main__":
    is_anagram("heart", "earth")  # True
    is_anagram("python", "typhon")  # True
    is_anagram("hello", "world")  # False
    is_anagram("ab", "abc")  # False