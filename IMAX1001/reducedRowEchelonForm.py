import sympy


def solveMatrix(arr):
    return sympy.Matrix(arr).rref()


M = [[], [], []]

print(reduceMatrix(M))
