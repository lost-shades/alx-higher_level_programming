#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elements in row:
            print("{:d}".format(elements), end=" " if i_col != i_row[-1] else "")
        print()
