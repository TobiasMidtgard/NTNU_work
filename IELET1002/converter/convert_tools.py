def decimalToBinary(n):
    return bin(n).split('b')[-1]


def decimalToOct(n):
    return oct(n).split('o')[-1]


def decimalToHex(n):
    return hex(n).split('x')[-1]


def binaryToOct(n):
    return oct(int(str(n), 2)).split('o')[-1]


def binaryToDecimal(n):
    return int(str(n), 2)


def binaryToHex(n):
    return hex(int(str(n), 2)).split('x')[-1]


def octToBinary(n):
    return bin(int(str(n), 8)).split('b')[-1]


def octToDecimal(n):
    return int(str(n), 8)


def octToHex(n):
    return hex(int(str(n), 8)).split('x')[-1]


def hexToBinary(n):
    return bin(int(str(n), 16)).split('b')[-1]


def hexToOct(n):
    return oct(int(str(n), 16)).split('o')[-1]


def hexToDecimal(n):
    return int(str(n), 16)
