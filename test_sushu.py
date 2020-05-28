# ***********************************************************************************
# Author: dwl
# Time:   2020.05.22
# Description: 例子：输入一个数，判断它是不是素数
#
# ***********************************************************************************


def s_pri(num):
    if num < 2:
        return num, "这个数不是素数"
    else:
        if num == 2:
            return num, "这个数是素数"

        for i in range(2, num):
            if (num % i) == 0:
                return num, "这个数不是素数"
        else:
            return num, "这个数是素数"


if __name__ == "__main__":
    num1 = int(input("请输入一个正整数："))
    print(s_pri(num1))

