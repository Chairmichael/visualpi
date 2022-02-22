# primepixels.py
# Creates an image from primes

from itertools import zip_longest
from math import sqrt
from PIL import Image
import numpy as np


def image_from_double_primes(size):
    size = int(size)
    arr = np.zeros((size, size, 3), dtype=np.uint8)
    primes_list = primes(int(size**2)+1)

    double_primes_list = []
    for x, y in zip_longest(primes_list, primes_list[1:]):
        # x = p_n, y = p_n+1 (the prime after p)
        if y != None and y - x == 2:
            double_primes_list.append(x)

    # Switch pixels when their position is a prime
    for n in double_primes_list:
        arr[n // size][n % size] = [255, 255, 255]
        arr[(n+2) // size][(n+2) % size] = [255, 255, 255]

    new_image = Image.fromarray(arr)
    new_image.save('double-primes.png')


def image_from_primes(size):
    size = int(size)
    arr = np.zeros((size, size, 3), dtype=np.uint8)
    primes_list = primes(int(size**2)+1)
    # Switch pixels when their position is a prime
    for n in primes_list:
        arr[n // size][n % size] = [255, 255, 255]

    new_image = Image.fromarray(arr)
    new_image.save('primes.png')


# http://rebrained.com/?p=458
def primes(upto=1000000):
    primes = np.arange(3, upto+1, 2)
    isprime = np.ones((upto-1)//2, dtype=bool)
    for factor in primes[:int(sqrt(upto))]:
        if isprime[(factor-2)//2]:
            isprime[(factor*3-2)//2::factor] = 0
    return np.insert(primes[isprime], 0, 2)


if __name__ == '__main__':
    length = 10**3  # Length of one edge of the image
    # image_from_primes(length)
    image_from_double_primes(length)
