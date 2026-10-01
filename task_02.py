def bytes_to_kilobytes(value):
    return value / 1024
print(bytes_to_kilobytes(2048))
def kilobytes_to_bytes(value):
    return value * 1024
if __name__ == "__main__":
    print(bytes_to_kilobytes(2048))
    print(kilobytes_to_bytes(2))
