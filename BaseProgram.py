import random

""" Funkcia na detekciu prvočísiel """
def is_prime(N: int) -> bool:
    
    if not isinstance(N, int) or N <= 1:
        return False
    elif N == 2:
        return True
    elif N % 2 == 0:
        return False
    else:
        ukazovatel = 3
        while ukazovatel * ukazovatel <= N:
            if N % ukazovatel == 0:
                return False
            ukazovatel += 2       
    return True

""" Funkcia na faktorizáciu čísiel """
def factorize(N: int) -> list[int]:

    if not isinstance(N, int):
         raise ValueError("Nedefinovaný vstup - iba celé čísla")
    else:
        factors = []
        if N < 0:
            factors.append(-1)
            N *= -1
            
        ukazovatel = 2
        while ukazovatel * ukazovatel <= N:
            if N % ukazovatel == 0:
                factors.append(ukazovatel)
                N //= ukazovatel
            else:
                ukazovatel += 1

        if N > 1:
            factors.append(N)

    return factors

""" Funkcia pre Legendrov symbol """
def Legendre(A: int, P: int) -> int:

    if not isinstance(A, int):
        raise ValueError("Nedefinovaný vstup - iba celé čísla")

    if not is_prime(P) or P == 2:
        raise ValueError("Nedefinovaný vstup - menovateľ musí byť nepárne prvočíslo")

    if A % P == 0:
        return 0

    if A == 1:
        return 1

    if A == -1:
        return int((-1)**((P-1)/2))
    
    if A == 2:
        return int((-1)**((P**2 -1)/8))

    factors = factorize(A)

    if -1 in factors:
        A *= -1
        return Legendre(-1, P) * Legendre(A, P)

    if A != (A % P):
        return Legendre(A % P, P)
    
    if len(factorize(A)) > 1:
        legendre_product = 1
        for factor in factors:
            legendre_product *= Legendre(factor, P)
        return legendre_product

    quad_recip = int((-1)**(((A-1)*(P-1))/4))

    return quad_recip * Legendre(P, A)

""" Funkcia pre Jacobiho symbol """
def Jacobi(A: int, N: int) -> int:

    if not isinstance(A, int) or not isinstance(N, int):
        raise ValueError("Nedefinovaný vstup - iba celé čísla")

    if N <= 0 or N % 2 == 0:
        raise ValueError("N musí byť nenulové nepárne kladné číslo")

    if A % N == 0:
        return 0

    if A == 1:
        return 1

    if A == -1:
        return int((-1)**((P-1)/2))

    if A == 2:
        return int((-1)**((N**2 -1)/8))

    if A != (A % N):
        return Jacobi(A % N, N)

    parity = 0

    while A % 2 == 0:
        parity += 1
        A //= 2

    factors = factorize(N)

    result_1 = 1
    
    if parity > 0:
        for factor in factors:
            result_1 *= Legendre(2, factor)
        result_1 = result_1**parity

    if A == 1:
        return result_1
    else:
        result_2 = ((-1)**(((A-1)*(N-1))/4)) * Jacobi(N, A)

    result = int(result_1 * result_2)

    return result

""" Funkcia pre Solovay-Strassenov test """
def Sol_Stra_test(N: int, iterations: int) -> bool:
    
    if N < 2 or N % 2 == 0:
        return False

    if N == 2:
        return True

    for _ in range(iterations):
        
        num = random.randint(2, N)
        
        jacobi_symbol = Jacobi(num, N)
        
        modular_exponentiation = pow(num, (N - 1) // 2, N)

        if jacobi_symbol % N != modular_exponentiation % N:
            return False

    return True

