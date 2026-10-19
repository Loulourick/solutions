def quirky_numbers(k):
    res = []
    pow = 10 ** k
    for s in range (2 * pow):
        kvad = s * s
        pol1 = kvad // pow
        pol2 = kvad % pow
        if pol1 + pol2 == s:
            res.append(str(pol1).zfill(k) + str(pol2).zfill(k))
    return res
if __name__ == "__main__":
    quirky_numbers(1)
    # ['00', '01', '81']

    quirky_numbers(2)
    # ['0000', '0001', '2025', '3025', '9801']