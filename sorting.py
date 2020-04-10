import Queue
import math

def radix_sort(array):
    q = [Queue.Queue() for i in range(10)]

    # determine number of digits
    digit = 0
    for num in array:
        digit = max(digit, int(math.log(num,10))+1)

    for i in range(digit):
        for num in array:
            q[(num/(10**i))%10].put(num)

        ni = 0
        for i in range(10):
            while not q[i].empty():
                array[ni] = q[i].get()
                ni += 1

    return array

if __name__ == '__main__':
    array = [321,142,5,81,19,391,25]
    assert radix_sort(array) == [5,19,25,81,142,321,391]