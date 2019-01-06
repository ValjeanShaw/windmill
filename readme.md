# 1. python基础
#python

> base.py
## 注释
两种注释方式：
* #   单行
* ’‘’多行单引号‘’‘    或者 “”“多行引号”“”


## 输入输出
* 输入：    input()
* 输出：    print()
print中字符串拼接有两种方式    “+”和”,”  前者正常拼接，后者拼接后，逗号将转化为空格
print(“hello”+”world”)
print(“hello”,”world”)


## 数据类型
Number三种类型：
1. 整形              num1=1
2. 浮点型         num2=1.2
3. 布尔类型     num3=True
4. 符合类型     num4=num1+num2

## 空值
None   相当于其他静态语言中的null



> dataConstruct.py
## 字符串
### 操作字符串
1. 截取     变量[开始下标：结束下标(不包含)]
2. 连接      +
3. 复制      *
### 格式化字符串
1. 占位符   %s等
2. format() 方法     
```'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)```
