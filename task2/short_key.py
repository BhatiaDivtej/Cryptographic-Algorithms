"""
N: the modulus

return (p, q): the factors of N
"""
def get_factors(N):
    # TODO: Implement this function for Task 2
    p, q = 0, 0
    
    # TODO: Implement this function for Task 2
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            p = i
            q = N // i
            break

    return p, q

"""
p, q: the factors of N
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_p_q_e(p, q, e):
    d = 0
    # TODO: Implement this function for Task 2
    d = pow(e, -1, ((p - 1) * (q - 1)))
    return d


def get_student_number():
    # TODO: Fill your student number here
    return "3035832438"
    
