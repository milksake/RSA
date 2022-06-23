# RSA CCOMP3-1

# Integrantes:
- Mariana Cáceres Urquizo
- Camila Orihuela Flores
- Jorge Núñez Paucar

# Instrucciones de ejecución
*Clonar*
```
git clone https://github.com/milksake/RSA.git
```
*Ejecutar*
```
python3 RSA.py
```
# [RSA.py](RSA.py)

rsaKeyGenerator(bits)
- Recibe como parámetro un número "K" de bits.
- Genera dos números primos (p,q) que ocupan la mitad de "K" bits cada uno.
- Multiplica los números (n=p*q)
- Halla phiN (phiN = phi(n))
	- phi(n): Halla la cantidad de números 		coprimos menores a "n" con respecto a "n"
- Genera un número "e" tal que sea coprimo con phiN
- Halla la inversa de "e" (d = inversa(e))
	- (e*d) es congruente con 1 en módulo n
- Retorna los valores "e", "d" y "n"

rsaCipher(mensaje, llaves)
- Cifra el "mensaje" usando la llave "e" y "n"
- Descifra el "mensaje" usando la llave "d" y "n"
