"""
#函数
    工程思想、模块化
    ·代码的一种组织形式
    ·一个函数一般完成一项特定的功能
    ·函数使用
        ·函数需要先定义，只是定义的话函数不会执行
        ·使用函数，俗称调用
            ·直接函数名后面跟括号
        ·def关键字，后跟一个空格
        ·函数名，自己定义，起名需要遵循命名规则，约定俗成，大驼峰命名只给类用
        ·后面括号和冒号不能省，括号内可以有参数
        ·函数内所有代码缩进
        ·见 代码片段1
    ·函数的参数和返回值
        ·参数：负责给函数传递一些必要的数据或者信息
            ·形参（形式参数）：在函数定义的时候用到的参数，没有具体值，只是一个占位的符号，称为形参
            ·实参（实际参数）：在调用函数的时候输入的值
        ·返回值：函数的执行结果
            ·使用return关键字
            ·如果没有return，默认返回一个none
                ·见 代码片段3
            ·函数一旦执行return语句，则无条件返回，即结束函数的执行
                ·见 代码片段4
        ·参数的定义和使用
        ·见 代码片段2
    ·查找函数帮助文档
        ·见 代码片段5
"""

# 代码片段1
def func():
    print("我是一个函数")
    print("我要完成一定功能")
    print("我结束了")
func()

# 代码片段2
# 参数person只是一个符号，代表的是调用的时候的某一个数据
# 调用的时候，会用p的值代替函数中的所有的person
def hello(person):
    print(" {0},你怎么了".format(person))
    print("Sir,你不理我我就走了")
p = "明月"
hello(p)

# 代码片段3
# return语句的基本使用。函数打完招呼后返回一句话
def hello(person):
    print(" {0},你怎么了".format(person))
    print("Sir,你不理我我就走了。")
    return "我已经跟 {0} 打完招呼了， {1} 不理我。".format(person,person)
p = "明月"
rst = hello(p)
print(rst)

# 代码片段4
def hello(person):
    print(" {0},你怎么了".format(person))
    return "哈哈，我提前结束了"
    print("Sir,你不理我我就走了。")
    return "我已经跟 {0} 打完招呼了， {1} 不理我。".format(person,person)
p = "东东"
rst = hello(p)
print(rst)

# 九九乘法表
# print函数默认任务打印完毕后换行
for row in range(1,10):
    for col in range(1,row+1):
        #={2}等号之前留两个空格就对不齐，留其他个数的空格都能对齐？
        print("{1}*{0}={2}".format(row,col,row*col),end="\t")
    print()
# 代码片段5
# help(print)










