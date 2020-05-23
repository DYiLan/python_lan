# ***********************************************************************************
# Author: huanghc
# Time:   2020.05.21
# Description: 测试递归函数，例子：斐波那契数列的求和
#
# ***********************************************************************************


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_sum(n):
    rst = 0
    for i in range(1, n+1):
        print("i: ", i)
        fib_rst = fib(i)
        print("fib_rst: ", fib_rst)
        rst += fib_rst
        print("rst: ", rst)
    return rst


if __name__ == "__main__":
    # print(fib(20))
    print(fib_sum(50))



