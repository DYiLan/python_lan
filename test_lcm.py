# ***********************************************************************************
# Author: dwl
# Time:   2020.05.28
# Description: 例子：输入两个正整数，计算它们的最小公倍数
#
# ***********************************************************************************


def lcm(x, y):
    if x > y:
        larger = x
    else:
        larger = y

    while True:
        if (larger % x == 0) and (larger % y == 0):
            lcm1 = larger
            break
        larger += 1

    return lcm1


if __name__ == "__main__":
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    print(num1, "和", num2, "最小公倍数是：", lcm(num1, num2))

