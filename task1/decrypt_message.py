
"""
N: the modulus
e: the encryption exponent
d: the decryption exponent
c: the encrypted message

return m: the plain text
"""
def decrypt_message(N, e, d, c):
    m = 0
    # TODO: Implement this function for Task 1
    m = pow(c, d, N)  # Calculate c^d mod N
    return hex(m).rstrip('L')

def get_student_number():
    # TODO: Fill your student number here
    return "3035832438"
    
