from euclides import euclidesExt

def inverso(a, n):
    (mcd, x, y) = euclidesExt(a, n)
    if mcd == 1:
        return x % n
    else:
        return None
