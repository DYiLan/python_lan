# ***********************************************************************************
# Author: huanghc
# Time:   2020.05.22
# Description: str 变量类型举例
#
# ***********************************************************************************


if __name__ == '__main__':
    str1 = "daiwanglan shi shabi"
    str2 = 'huanghc hen niubi'
    str3 = """dwl henxihuan bei ma"""
    str31 ="""窗前明月光，
疑是地上霜。
举头望明月，
低头思故乡。"""
    print(str31)

    str4 = "let's go"
    str5 = 'Your Name is "dshabi"'
    print(str5)
    str6 = """C:\\Users\\Administrator\\Desktop\\python\\get_result"""
    print(str6)
    str7 = 'let\'s\n go \nto \nhotel'
    print(str7)
    str8 = "123456\t678"
    print(str8)
    str9 = r"C:\Users\Administrator\Desktop\python\get_result"
    print(str9)
    index5 = str5.rfind("dsaaaahabi")
    print(index5)
    str10 = "t"
    if str10 not in str6:
        print(str5)
    else:
        print(str6)

    str11 = str5 + str6
    list1 = [str5, str6]
    str12 = ''.join(list1)
    str13 = "1".join(str5)
    print(len(str13), str13)
    str14 = "1234567890"
    print(str14.rindex("90"))
    list2 = str31.split('\n')
    print(list2)
    list3 = str31.splitlines()
    print(list3)
    list4 = str9.partition("t")
    print(list4)





