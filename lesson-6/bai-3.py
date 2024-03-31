# bài 3 - quiz
def get_answer(text):
    print(text)
    while True:
        inp = input(">>> ")
        if inp.lower() in ("a", "b", "c", "d"):
            return inp.lower()
        print("Nhập A, B, C hoặc D")

cau1 = get_answer(
"""Python phát hành năm nào?
    A. 1991
    B. 1989
    C. 2020
    D. 2001"""
) == "a"

cau2 = get_answer(
"""Ai đã tạo ra Python?
    A. Steve Jobs
    B. Dennis Ritchie
    C. Guido van Rossum
    D. James Gosling"""
) == "c"

cau3 = get_answer(
"""In ra 'Hello world' trong Python như thế nào?
    A. System.out.println('Hello world')
    B. print('Hello world')
    C. console.log('Hello world')
    D. puts 'Hello world'"""
) == "b"

cau4 = get_answer(
"""Trong Python, in ra (0.1 + 0.2) sẽ ra cái gì?
    A. 0.3
    B. 3/10
    C. 0.1 + 0.2
    D. 0.30000000000000004"""
) == "d"

sum = (cau1 + cau2 + cau3 + cau4)
print(f"Câu trả lời đúng: {sum}/4")
if sum == 4:
    print("Hoan hô! Bạn trả lời đúng hết!")