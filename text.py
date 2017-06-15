import random
total = 0
times = 0
while Ture:
    choice = input("1.开始游戏 2.结束\n")
    if str(choice) == "1":
        total += 1
        num = random.randint(1,100)
        print("猜一个1-100间的整数:")
        while True:
            times += 1
            answer = int(input())
            if answer < num:
                print(answer,"你猜的太小了")
            elif answer > num:
                print(answer,"你猜的太大了")
            else:
                print("你猜对了！")
                break
    elif str(choice) == "2":
        break
    if total > 0:
        print("共猜了%d 次，平均%.1f次猜中\n"%(total,float(times)/total)
print("游戏结束")
