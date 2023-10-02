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
        
    # Calculate the product of all moduli
    N = N1 * N2 * N3
    
    # Calculate partial moduli
    N1_bar = N // N1
    N2_bar = N // N2
    N3_bar = N // N3
    
    # Calculate modular inverses
    M1 = modinv(N1_bar, N1)
    M2 = modinv(N2_bar, N2)
    M3 = modinv(N3_bar, N3)
    
    # Use CRT to compute the message
    m = (C1 * N1_bar * M1 + C2 * N2_bar * M2 + C3 * N3_bar * M3) % N
    
    # Calculate the cubic root of m to get the original message
    original_message = root3(m)
    
    # Convert the original_message to hexadecimal format
    hex_message = hex(original_message).replace("0x", "")
    
    return "0x" + hex_message
 

def get_student_number():
    # TODO: Fill your student number here
    return "3035832438"
    
