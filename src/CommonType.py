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
