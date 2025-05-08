#!/usr/bin/env python3

def print_fibonacci(length):
    
    '''prints fibonacci sequence of length n'''
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return
    fib = [0, 1]
    for i in range(2, length):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)
    pass