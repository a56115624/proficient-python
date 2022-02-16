# x = 0
# while x<10:
#     x =x+1
#     print(x) 



# 我現在想從 10 印到 1, times=0~9, 我就用 times 改出來
# times = 0
# while times<10:
#     print(10-times,"Hello")
#     times = times+1


 # 我現在想從 2 開始每次跳兩個, 2, 4, 6, ... 十次
# jump = 0
# while jump<10:
#     print(2*(jump+1))
    # jump = jump+1


#  問題：從 1 + 2 + 3 + … + 10 等於多少
# x = 0
# for i in range(5,51,5):
#     x = x+i
# print(x)

#計算1到100間，所有數字的平方和 (338350)
# x = 0
# for i in range(1,101):
#     x = x + i**2
# print(x)
# enumerate 列舉
# word = 'hello'
# for i in enumerate(word):
#     print(i)


#不使用 enumerate()
# i = 0
# word = 'hello'
# for value in word:
#     print(i, word[i])
#     i += 1

#使用enumerate()
# word = 'hello'
# for i in enumerate(word):
#     print(i)

# 用兩個變數一樣可以
# word = 'hello'
# for index, value in enumerate(word):
#     print(index, type(index))


# 加入\n可以插入間隔
breakfast = ['eggs', 'milk', 'apples', 'sandwiches']
for food in breakfast[0:2]:
    print('I love ' + food.upper() + ' so much.')
    print('I want to have ' + food.upper() + ' as my breakfast!\n')