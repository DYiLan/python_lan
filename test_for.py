
stu_list = ["小明", "小红", "小黄"]
for stu in stu_list:
    if stu == "小明":
        print("找到你了")
        break
    else:
        print(stu, "对不起，认错人了")
else:
    print("找到小黄了，我们去玩")

num_list = range(1, 10)
print(list(num_list))

for num in num_list:
    if num == 5:
        print("找到5了")
        continue
    elif num == 6:
        print("找到6了")
    else:
        pass

    print(num, "继续查找下一个")


