"""tam giác"""
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if not ((a + b > c) and (a + c > b) and (b + c > a)):
#     print("ko phải tam giác")
# else:
#     # print("là tam giác")
#     sides = [a, b, c]
#     hypo = max(sides)
#     sides.remove(hypo)
#     leg1, leg2 = sides

#     if leg1**2 + leg2**2 == hypo**2:
#         print("tam giác vuông")
#     elif a == b == c:
#         print("tam giác đều")
#     else:
#         print("tam giác thường")

"""điểm TB"""
# a = int(input("toán: "))
# b = int(input("văn: "))
# c = int(input("anh: "))
# avg = (a + b + c)/3

# if avg < 5:
#     print("chưa đạt")
# elif avg < 7:
#     print("đạt")
# elif avg < 8:
#     print("khá")
# else:
#     print("tốt!!!")

"""BMI"""
# weight = float(input("cân nặng (kg): "))
# height = float(input("chiều cao (m): "))
# bmi = weight / (height**2)

# if bmi < 16:
#     print("gầy cấp độ III")
# elif bmi < 17:
#     print("gầy cấp độ II")
# elif bmi < 18.5:
#     print("gầy cấp độ I")
# elif bmi < 25:
#     print("bình thường")
# elif bmi < 30:
#     print("thừa cân")
# elif bmi < 35:
#     print("béo phì cấp độ I")
# elif bmi < 40:
#     print("béo phì cấp độ II")
# else:
#     print("béo phì cấp độ III")

"""if else"""
# a = int(input("cho một số: "))
# print("đạt" if a > 5 else "ko đạt")