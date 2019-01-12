# key:value  {}
dict1 = {"name": "xiaoran", "age": "23", "sex": "male"}
print(dict1)

# 获取
sex = dict1['sex']
print(sex)
print(dict1.get('x','er'))

print(dict1.keys())

# 修改
dict1['age'] = 18
print(dict1)

# 新增元素
dict1['province'] = '四川'
print(dict1)

# 删除，清除
# 删除元素
del dict1['age']
print(dict1)

# 清除
dict1.clear()
print(dict1)

# 删除字典
del dict1