import math
# for num1 in range(1, 10):
#     for num2 in range(1, 10):
#         if num2 < num1:
#             print(num1 * num2, end=" ")
#         elif num2 == num1:
#             print(num1 * num2)
#         else:
#             break


def print_99(num3):
    a = True
    for num1 in range(1, num3):
        for num2 in range(1, num1 + 1):
            print(num1 * num2, end=" ")
            a = False
        print()

    if num3 - a > 10:
        return None
    else:
        print("this is end")

    return None


result1 = print_99(11)
if result1 == None:
    print(result1)

