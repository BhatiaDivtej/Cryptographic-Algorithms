"""
N: the modulus

return (p, q): the factors of N
"""
def get_factors(N):
    # TODO: Implement this function for Task 2
    p, q = 0, 0

    # Function checks if a number is prime or not.
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    # Iterating from 2 to sqrt(N)+1
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            if is_prime(i) and is_prime(N // i):
                p = i
                q = N // i
                return p, q
            
    return p, q

"""
p, q: the factors of N
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_p_q_e(p, q, e):
    d = 0
    # TODO: Implement this function for Task 2
    
    # Phi is the totient
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return d


def get_student_number():
    # TODO: Fill your student number here
    return "3035832438"
    
