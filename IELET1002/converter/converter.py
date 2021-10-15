import convert_tools as cv


def convert(num, base):  # base options: 2, 8, 10, 16

    if base == 2:
        return f"Octal: {cv.binaryToOct(num)}\nDecimal: {cv.binaryToDecimal(num)}\nHex: {cv.binaryToHex(num)}"

    if base == 8:
        return f"Binary: {cv.octToBinary(num)}\nDecimal: {cv.octToDecimal(num)}\nHex: {cv.octToHex(num)}"

    if base == 10:
        return f"Binary: {cv.decimalToBinary(num)}\nOctal: {cv.decimalToOct(num)}\nHex: {cv.decimalToHex(num)}"

    if base == 16:
        return f"Binary: {cv.hexToBinary(num)}\nOctal: {cv.hexToOct(num)}\nDecimal: {cv.hexToDecimal(num)}"


# Hvis du skal konvertere fra hex med f.eks: af3 så må det skrives som string
if __name__ == "__main__":
