import random
me = int(input("[0]棒子 [1]老虎 [2]雞 [3]蟲"))
com = random.randint(0,3)
tans = ("棒子","老虎","雞","蟲")
print("妳的物品",tans[me])
print("電腦的物品",tans[com])
if me == com:
    print("平手")
elif me == (com+1)%4:
    print("妳輸了了")
else:
    print("妳贏了")