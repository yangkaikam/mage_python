# 输入一个数字,判断其长度,并从高位向低位显示

# 自编写for循环
# num = input("输入一个数字:")
# length = int(len(num))
# w = 10 ** (length-1)
# num = int(num)
# flag = False
# for i in range(1, length+1):
#     t = num // w
#     num = num % w
#     w = w // 10
#     if t:
#         flag = True
#     if flag:
#         print(t)


# 教学使用flag开关控制,while循环
num = input("输入一个数字:")
length = int(len(num))
num = int(num)
w = 10 ** (length-1)
count = 0
flag = False
while w:
    t = num // w
    if t:
        flag = True
    if flag:
        print(t)
        count += 1
    num = num % w
    w = w // 10
print("输入的是%d位数" % count)