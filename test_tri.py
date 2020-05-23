# ***********************************************************************************
# Author: dwl
# Time:   2020.05.21
# Description: 例子：判断是否构成三角形，并输出它的面积和周长
#
# ***********************************************************************************
import math


def tri_1(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print("构成三角形")
        t = a + b + c
        p = t / 2
        s = math.sqrt(p * ((p - a) * (p - b) * (p - c)))
        return "三角形的周长:", t, "三角形的面积:", s
    else:
        return "不能构成三角形"


if __name__ == "__main__":
    a1 = float(input('a1 = '))
    b1 = float(input('b1 = '))
    c1 = float(input('c1 = '))
    print(tri_1(a1, b1, c1))




