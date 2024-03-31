# nums = [34, 4, 7, 234, 7, 2]
# sum = 0

# for n in nums:
#     sum += n

# print("the sum is:", sum)

#####

a = ["hi", "bye", "hello"]

i = 0
while i < len(a):
    if a[i] == "bye":
        i += 1
        continue
    print(a[i])
    i += 1


#####

# nums = [1, 2, 3, 4]
# alpha = ["a", "b", "c", "d"]
# for num in nums:
#     print(num, end=" ")
#     for alp in alpha:
#         print(alp, end=" ")