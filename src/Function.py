# 函数
def voice():
    print("this is voice")


voice()


# 带参数   按顺序传参和指定具体参数
def voice(param1, param2):
    print("this param form 1 to 2 is :", param1, param2)


voice("cat", "dog")
voice(param1="param2", param2="param1")


# 默认参数
def voice(param1, param2="babala"):
    print("this param form 1 to 2 is :", param1, param2)


voice("cat")


# 带上返回值
def cal(param1, param2, type):
    if type == "+":
        return param1 + param2
    elif type == "-":
        return param1 - param2
    elif type == "*":
        return param1 * param2
    elif type == "/":
        return param1 / param2
    elif type == "%":
        return param1 % param2


print("+", cal(9, 4, "+"))
print("-", cal(9, 4, "-"))
print("*", cal(9, 4, "*"))
print("/", cal(9, 4, "/"))
print("%", cal(9, 4, "%"))
