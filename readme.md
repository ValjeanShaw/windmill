# python基础

# 入门基础和数据类型
> Base.py
## 注释
两种注释方式：
* '#' 单行
* ’‘’多行单引号‘’‘    或者 “”“多行引号”“”


## 输入输出
* 输入：    input()
* 输出：    print()
print中字符串拼接有两种方式    “+”和”,”  前者正常拼接，后者拼接后，逗号将转化为空格
print(“hello”+”world”)
print(“hello”,”world”)


## 基本数据类型
Number三种类型：
1. 整形              num1=1
2. 浮点型         num2=1.2
3. 布尔类型     num3=True
4. 符合类型     num4=num1+num2

## 空值
None   相当于其他静态语言中的null

------
# 常用类型
> CommonType.py
## 字符串
### 操作字符串
1. 截取     变量[开始下标：结束下标(不包含)]
2. 连接      +
3. 复制      *
### 格式化字符串
1. 占位符   %s等
2. format() 方法     
```'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)```

## 列表

定义方式 [] 
list=[‘’,’’,’’]
### 操作列表
1. 索引    list[0]
2. 切片    
* list[0:1]   
* list[1:]
* list[-1]  负数表示倒数第几位
### 列表的一些常用函数
* append()
* sort()
* insert()
* remove(具体值)
* del (list[1])

## 元组

定义方式（）
tuple=('','')

### 操作列表
1. 索引  tuple[0]
2. 切分  tuple[0:2]
* tuple[0:1]   
* tuple[1:]
* tuple[-1]  负数表示倒数第几位

### 元组的一些常用函数
* tuple("list")

## 字典

定义方式 {}
dict={'key':'value','key':'value'}

### 操作列表
1. 取值  dict[key] 
2. 追加  dict['newKey']='newValue'


### 字典的一些常用函数
* del dict['key']
* del dict
* dict.clear()
* dict.get(key,defaultValue) 

## set

定义方式 set([])
set1=set([1,2,3])

### 操作列表
不能取值，访问set值就是判断set中是否存在该值
[key] in [set]

## 与或非的操作
与 and  或  or   非  not

注意，不是 &&，||和！来表示了

## 函数
### 定义
```def [functionName]([param...])```

* 返回值不需要定义，直接return
* 多个函数名可以重复，参数需要不同
* 参数可以指定顺序，并且可以指定默认值

## 对象和类
### 定义
``` class [className]([object])```

### 属性和方法

#### 普通属性
__init__()构造函数中定义

#### 私有属性
属性前加"__"   ```__fiels__```

#### 隐藏属性
不定义的属性，在操作中可以直接使用

#### 类属性
在类的中定义，不在__init__方法中定义

#### 构造方法
``` def __init__(self,(fields...))```

#### 普通方法
``` def [methodname](self,(fields...))```

#### 私有方法
```def __[methodname](self,(fields...))```

#### 类方法
```
@classmethod
def [methodname](cls,(fields...))
```

#### 静态方法
```
@staticmethod
def [methodname]()
```

### 继承
#### 多继承
1. 可深度继承，多层级的继承
2. 并行继承 
``` class [className]([object1],[object2])```
子类继承父类方法，会从前到后检索，相同定义的方法，排在前面的会被调动

#### 重写父类方法
命名相同，参数可重写