from primeNGenerator import genPrimoBits, randomBits
from euclides import euclides
from inverso import inverso
from expMod import expMod

def rsaKeyGenerator(bits):
    # Generar numeros primos p y q
    p = genPrimoBits(bits // 2)
    q = genPrimoBits(bits // 2)
    while p == q:
        q = genPrimoBits(bits // 2)
    # Calcular n = p * q
    n = p * q
    # Calcular phi(n)
    phiN = (p - 1) * (q - 1)
    # Generar e, tal que mcd(e, phiN) = 1
    e = randomBits(bits)
    while euclides(e, phiN) != 1:
        e = randomBits(bits)
    # Hallar d (la inversa de e)
    d = inverso(e, phiN)
    return ([e, n], [d, n])

def rsaCipher(m, k):
    return expMod(m, k[0], k[1])

if __name__ == "__main__":
    (P, S) = rsaKeyGenerator(64)
    print(P, S)
    m = int(input("Ingrese un numero: "))
    c = rsaCipher(m, P)
    print(m, c, rsaCipher(c, S))