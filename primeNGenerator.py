from millerRabin import MillerRabin
from random import randint

def randomBits(b):
    pow2 = pow(2, b - 1)
    n = randint(0, pow2  * 2 - 1)
    m = pow2 + 1
    n = n | m
    return n

def genPrimoBits(b, s = 30):
    n = randomBits(b)
    while not MillerRabin(n, s):
        n = n + 2
    return n

def genPrimoMayor(n, s = 30):
    n = n + 1 - (n % 2)
    while not MillerRabin(n, s):
        n = n + 2
    return n
