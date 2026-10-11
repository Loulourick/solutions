from data.morse import morse
def to_morse(text):
    words = text.split()
    result = []
    for word in words:
        j = []
        for i in word:
            j.append(morse[i])
        result.append("".join(j))
    return " / ".join(result)

def from_morse(code):
    reverse_morse = {code: letter for letter, code in morse.items()}
    words = code.split()
    result = []
    for word in words:
        code1 = word.split()
        h = ""
        for i in code1:
            h += reverse_morse[i]
        result.append(h)
    return " "/join(result)

if __name__ == "__main__":
    to_morse("PYTHON 3")
    # '.--. -.-- - .... --- -. / ...--'

    to_morse("SOS")
    # '... --- ...'

    from_morse('.--. -.-- - .... --- -. / ...--')
    # 'PYTHON 3'

    from_morse('... --- ...')
    # 'SOS'