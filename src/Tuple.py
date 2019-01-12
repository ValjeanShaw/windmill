# 元组   元素不可变  小括号表示
tuple1 = ("yuan", "zu", "123")

# 切分
print(tuple1[0:2])
print(tuple1[0])
print(tuple1[-1])

# 列表转换成元组
list1 = ["1", "2", "3"]
tuple2 = tuple(list1)
print(tuple2)

# 获取
print(tuple2[1])

# 删除
del tuple1
