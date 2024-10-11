import random
from sympy import isprime
import os

# Hàm để tính UCLN của hai số
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tìm số mũ ngược của a modulo m, sử dụng Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Tạo khóa RSA
def generate_keypair(bits):
    p = q = 1
    while not isprime(p):
        p = random.getrandbits(bits)
    while not isprime(q) or p == q:
        q = random.getrandbits(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

# Sử dụng ví dụ
bits = 8  # Số bit cho khóa
path =os.path.dirname(os.path.abspath(__file__)) #đường dẫn đến thư mục
public_key, private_key = generate_keypair(bits)

print(path)

print("Khóa công khai:", public_key)
# Lưu kết quả vào một tệp văn bản
with open(path+"/public_key.txt", "w") as f:
    f.writelines(str(public_key[0]) + " "+ str(public_key[1]))
    print("Đã lưu danh sách tệp Word vào 'public_key.txt'.")

print("Khóa riêng:", private_key)
# Lưu kết quả vào một tệp văn bản

with open(path+"/private_key.txt", "w") as ff:
    ff.writelines(str(private_key[0]) + " "+ str(private_key[1]))
    print("Đã lưu danh sách tệp Word vào 'private_key.txt'.")