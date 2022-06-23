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
    m_list=[]
    print(P, S)
    print('{:^20}{:^20}{:^20}'.format('m', 'c', 'm\''))
    for i in range(10):
        m = randomBits(32)
        while m in m_list:
            m = randomBits(32)
        m_list.append(m)
        c = rsaCipher(m, P)
        print('{:^20}{:^20}{:^20}'.format(m, c, rsaCipher(c, S)))
