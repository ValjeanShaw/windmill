# 列表
list = []

# 追加
list.append("12")
list.append("hello")
list.append("list")
# 排序
list.sort()
list.append(302)
print("append结果:", list)

# 插入
list.insert(3, "foreach")
print("insert结果:", list)


# 删除
list.remove(302)
print("remove结果:", list)

# 删除元素
del list[1]
print("remove结果:", list)

# 删除列表
del list
