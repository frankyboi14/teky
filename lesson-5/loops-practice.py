# B1: tổng số chia hết cho 3 trong 1-100
# sum = 0
# for i in range(1, 100 + 1):
#     if i % 3 == 0:
#         sum += i
# print("sum of numbers divisible by 3:", sum)

# B2: đếm số chẵn trong 1-50
# sum = 0
# for i in range(1, 50 + 1):
#     if i % 2 == 0:
#         sum += i
# print("sum of numbers divisble by 2:", sum)

# B3:
def is_prime(n):
    prime = True
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime

for i in range(25):
    print(i, "\t", "prime" if is_prime(i) else "not prime")