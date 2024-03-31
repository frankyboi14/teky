# bài 1
def is_prime(n):
    prime = True
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime

while True:
    try:
        inp = input("Các số nguyên tố từ 1 đến: ")
        inp = int(inp)
        break
    except:
        print("Hãy nhập một số nguyên.")

for i in range(inp + 1):
    print(i, "\t", "là" if is_prime(i) else "không phải là", "số nguyên tố")