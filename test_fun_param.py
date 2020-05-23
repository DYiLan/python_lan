# 20200519


def fun1(a, b=0, c=0):
    print(a, b, c)


def fun2(a=0):
    print(a)


def fun3(*a):
    print(a, type(a))


def fun4(**a):
    print(a, type(a))






c = 9
fun1(1, 2, 3)
fun1(c=7, a=c)
fun2()
fun3(1, 2, 3, "straa")
fun4(a=[1, 2, 3], b=(1, 2, 3), c="hggfgjf")


def fun5(a, b=67576576567567, *f, **d):
    print(a)
    print(b)
    print(f)
    print(d)


fun5(1, "jjjj", "ddddd" , x=6, y=7, z=8)


tuple_1 = (1,)
print(tuple_1, type(tuple_1))

