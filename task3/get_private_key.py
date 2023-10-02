### Get the greatest common divisor of 'a' and 'b'
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

"""
N1: your modulus
N2: your classmate's modulus

return result: True if n1 and n2 share the same prime number; otherwise, returns False
"""
def is_waldo(n1, n2):
    result = False
    # TODO: Implement this function for Task 3

    # Calculate the GCD of n1 and n2
    gcd_result = gcd(n1, n2)

    # they share a common prime factor if gcd result > 1
    if gcd_result > 1:
        return True
    else:
        return False    

"""
This function will be called if is_waldo(n1, n2) returns True.

N1: your modulus
N2: your classmate's modulus
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_n1_n2_e(n1, n2, e):
    # Calculate the GCD of n1 and n2
    gcd_result = gcd(n1, n2)

    # # Ensure that n1 and n2 share a common prime factor
    # if gcd_result == 1:
    #     raise ValueError("n1 and n2 do not share a common prime factor")

    # Calculate p and q, the prime factors of n1
    p = gcd_result
    q = n1 // gcd_result

    # Calculate phi(n1), where n1 = p * q
    phi_n1 = (p - 1) * (q - 1)

    # Calculate the modular multiplicative inverse of e modulo phi(n1)
    d = pow(e, -1, phi_n1)

    return d



def get_student_number():
    # TODO: Fill your student number here
    return "3035832438"
    
