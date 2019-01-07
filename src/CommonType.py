# 字符串
str = "english 中文字符也可以"
print(str)
print(str[1:3])
print(str * 2)

name = "abc"
nameByte = b"abc"
print(len(name))
print(len(nameByte))

string = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 注意浮点型可以选择小数点
print(string)

# 列表
listName = ["123", "hello", 999]
print(listName)
print(listName[1:])
print(listName[0: 1])
print(listName[-2])

# 与或非运算符
# 与 and  或  or   非  not
a = True
b = False
c = True

if (a and b):
    print("yes")
else:
    print("no")

if (a or b):
    print("yes")
else:
    print("no")

if (not not c):
    print("yes")
