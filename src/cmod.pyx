# cython: language_level=3

cdef extern from "util.h":
    int hello_4(int, int, int, int)

def square_from_bin(float x):
    return x * x

def hello_from_bin():
    print("Calling hello_4 with fixed args...")
    hello_4(0, 1, 2, 3)
