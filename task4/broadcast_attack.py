### Get the greatest common divisor of 'a' and 'b'
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

### Extended euclidean algorithm
def gcde(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcde(b % a, a)
        return g, x - (b // a) * y, y

"""
Get the modular inverse of 'b' under modulus 'a'
I.e., returns x that b * x mod a = 1
"""
def modinv(a, b):
    g, x, y = gcde(b, a)
    return x % a

### Get cube root of 'x'
def root3(x):
    h = 1
    while h ** 3 <= x:
        h *= 2
    l = h // 2
    m = 0
    while l < h:
        m = (l + h) // 2
        if m ** 3 < x and l < m:
            l = m
        elif m ** 3 > x and h > m:
            h = m
        else:
            return m
    return m + 1

"""
Nx: the x-th modulus
Cx: the x-th encrypted message

return m: the plain text

Note: m*m*m should be smaller than N1 * N2 * N3
"""
def recover_msg(N1, N2, N3, C1, C2, C3):
    m = 0
    # TODO: Implement this function for Task 4
    
    # Calculate the modular inverses
    m1 = N2 * N3
    m2 = N1 * N3
    m3 = N1 * N2

    # Calculate the partial decryptions using modular inverses
    x1 = C1 * modinv(m1, N1)
    x2 = C2 * modinv(m2, N2)
    x3 = C3 * modinv(m3, N3)

    # Calculate the final result using CRT
    M = (x1 + x2 + x3) % (N1 * N2 * N3)

    # Find the cube root of M to get the original message
    original_message = root3(M)
    
    return original_message


def get_student_number():
    # TODO: Fill your student number here
    return "3035832438"
    
