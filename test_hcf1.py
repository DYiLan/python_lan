# ***********************************************************************************
# Author: dwl
# Time:   2020.05.28
# Description: 例子：输入两个正整数，计算它们的最大公约数
#
# ***********************************************************************************


def gcd_1(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


if __name__ == "__main__":
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    print(num1, "和", num2, "最大公约数是：", gcd_1(num1, num2))
