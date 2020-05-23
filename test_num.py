import os
import math

if __name__ == '__main__':
    num = 0b111
    print(num, type(num))
    num1 = 0o101
    print(num1, type(num1))
    num2 = 0xFA0
    print(num2, type(num2))

    num = num2 = num3 = 1
    num, num1, num2 = 1, 2, 3
    pie = 3.1415926e3
    print(pie, type(pie))

    num = True
    num1 = 0 + num
    num2 = False
    num3 = 0 + num2
    print(num, num1, num2, num3)
    print(type(num), type(num1))

    num4 = 4 + 5j + 1
    print(num4, type(num4))

    num6 = 9 / 3
    print(num6, type(num6))
    num6 = 9 * 3
    print(type(num6))
    num6 = 9 // 4
    print(num6, type(num6))
    num6 = 9 % -4
    print(num6, type(num6))
    num = 3**3
    print(num)

    person1 = "man1"
    person2 = "man"
    gender = person1 > person2
    print(gender, type(gender))
    num1 = 0b1 << 30
    num2 = 0b1 >> 1
    num = num1 ^ num2
    print(num, num1, num2)

    if  ((num1 > 0) and (num2 < 0)):
        print("aaaa")

    str1 = "aabbcccccccccccccccccccccccccccc"
    str3 = "sadasdasdasdsadsad"
    str2 = "aabbcccccccccccccccccccccccccccc"
    print(str2 is str1)
    str1 = "aabbcccccccccccccccccccccccccccb"
    print(str1, str2)
    str1 = "aabbcccccccccccccccccccccccccccc"
    print(str2 is str1)
    print(id(str2), id(str1))

