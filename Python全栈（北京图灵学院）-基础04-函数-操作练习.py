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
        ·参数的定义和使用
        ·见 代码片段2
        ·参数：负责给函数传递一些必要的数据或者信息
            ·形参（形式参数）：在函数定义的时候用到的参数，没有具体值，只是一个占位的符号，称为形参
            ·实参（实际参数）：在调用函数的时候输入的值
            ·参数分类
                ·普通参数
                    ·参见代码片段2。定义的时候直接定义变量名。调用的时候直接把变量或者值放入指定位置。
                        def 函数名（参数1，参数2，……）
                            函数体
                        调用：调用的时候，具体值参考的是位置，按位置赋值
                        函数名（value1，walue2，……）
                ·默认参数
                    ·形参带有默认值。调用的时候，如果没有对相应参数赋值，则使用默认值。
                        def func_name(p1=v1,p2=v2,……):
                            func_bloc
                        调用1
                            func_name()
                        调用2
                            value1 = 100
                            value2 = 200
                            func_name(value1,value2)
                    ·见 代码片段6
                ·关键字参数
                    ·语法
                        def func(p1=v1,p2=v2,……)
                            func_body
                        调用函数：
                        func(p1=value1,p2=value2……)
                    ·比较麻烦，但是也有好处：不容易混淆，一般实参和形参只是按照位置一一对应即可，容易出错，使用关键字参数，可以不考虑参数位置。
                    ·见 代码片段7
                ·收集参数
                    ·把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
                    ·语法：
                        def func(*args):
                            func_body
                            # 按照list使用方式访问args得到传入的参数
                        调用：
                        func(p1,p2,p3,……)
                    ·参数名args不是必须这么写，但是我们推荐直接使用args，约定俗成
                    ·参数名args前面需要有星号
                    ·收集参数可以和其他参数共存
                    ·见 代码片段8
                    ·收集参数之关键字收集参数
                        ·把关键字参数以字典的格式存入收集参数
                        ·语法：
                            def func(**kwargs):
                                func_body
                            调用：
                            func(p1=v1,p2=v2,p3=v3,……)
                        ·kwargs 用此词一般约定俗成
                        ·调用的时候，把多余的关键字参数放入kwargs
                        ·访问kwargs需要按字典格式访问
                        ·见 代码片段9
                    ·收集参数混合调用的顺序问题
                        ·收集参数，关键字参数，普通参数可以混合使用
                        ·使用规则就是，普通参数和关键字参数优先
                        ·定义的时候一般按顺序找普通参数，关键字参数，收集参数tuple，收集参数dict
                        ·见 代码片段10
                    ·收集参数的解包问题
                        ·把参数放入list或者dict中，直接把list/dict中的值放入收集参数中
                        ·语法：
                            ·见 代码片段11
        ·返回值：函数的执行结果
            ·函数和过程的区别
                ·有无返回值
            ·使用return关键字，显示返回内容
            ·如果没有return，默认返回一个none
            ·推荐写法：无论有无返回值，最后都要以return结束
                ·见 代码片段3
            ·函数一旦执行return语句，则无条件返回，即结束函数的执行
                ·见 代码片段4
            ·返回值示例
                ·见 代码片段12
    ·函数的作用域
        ·变量作用域
            ·变量有作用范围限制
            ·分类：按照作用域分类
                ·全局（global）：在函数外部定义
                ·局部（local）：在函数内部定义
            ·变量的作用范围：
                ·全局变量：在整个全局范围都有效，全局变量在局部可以使用，即函数内部可以访问函数外部定义的变量
                ·局部变量：在局部范围可以使用，局部变量在全局范围无法使用
            ·LEGb原则：
                ·L（local）：局部作用域
                ·E（enclosing function locale）：外部嵌套函数作用域
                ·G（global module）：函数定义所在模块作用域
                ·b（buildin）：python内置模块的作用域
                ·总结：里边访问外边可以，外边访问里面不可以
        ·见 代码片段14
            ·提升局部变量为全局变量
                ·使用global
                ·见 代码片段15
            ·globals，locals函数
                ·可以通过globals和locals显示出全局变量和局部变量
                ·globals和locals函数叫内建函数
                ·见 代码片段16
            ·eval()函数
                ·把一个字符串当成一个表达式来执行，返回表达式执行后的结果
                ·语法：
                    eval（string_code,globals=None,locals=None）
                ·见 代码片段17
            ·exec（）函数
                ·跟eval功能类似，但是不返回结果
                ·语法：
                    exec（string_code，globals=None，locals=None）
                ·见 代码片段18
    ·递归函数
        ·函数直接或者间接调用自身
        ·优点：间接，理解容易
        ·缺点：对递归深度有限制，消耗资源大
        ·python对递归深度有限制，超过限制报错
        ·在写递归程序的时候，一定要注意结束条件
        ·见 代码片段19
        ·斐波那契例子
            ·一列数字，第一个值是1，第二个值也是1，从第三个开始，每一个数字的值等于前两个数字的值的和
            ·公式：f（1）=1，f（2）=1，f（n）=f（n-2）+f（n-1）
            ·如：1，1，2，3，5，8，13，……
            ·见 代码片段20
        ·汉诺塔例子
            ·每次只能移动一个盘子，任何时候大盘子在下面，小盘子在上面
            ·办法：
                ·1、n=1：直接把a上的一个盘子移动到c上面。a---->c
                ·2、n=2：
                    1、把小盘子从a移到b上，a---->b
                    2、把大盘子从a移到c上，a---->c
                    3、把小盘子从b移到c上，b---->c
                ·3、n=3：
                    1、把a上的两个盘子通过c移到b上去，调用递归实现
                    2、把a上剩下的一个最大盘子移到c上，a---->c
                    3、把b上两个盘子，借助a，移到c上去，调用递归
                ·4、n=n：
                    1、把a上的n-1个盘子，借助于c，移动到b上去，调用递归
                    2、把a上的最大盘子，也是唯一一个，移到c上，a---->c
                    3、把b上n-1个盘子，借助于a，移动到c上，调用递归
            ·见 代码片段21

# 函数文档
    ·函数的文档的作用是对当前函数提供使用相关的参考信息
    ·文档的写法：
        ·在函数内部开始的第一行使用三引号字符串定义符
        ·一般具有特定格式
        ·见 代码片段13
    ·查找函数帮助文档
        ·使用help函数，形如 help（func）
            ·见 代码片段5
        ·使用__doc__
            ·见 代码片段13
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

# 代码片段6
# 报名函数，需要知道学生性别。学习python的学生基本都是男生，所以，报名的时候如果没有特别指定，我们认为是男生
def reg(name,age,gender="male"):
    if gender == "male":
        print("{0} is {1} years old,and he is a good student".format(name,age))
    else:
        print("{0} is {1} years old,and she is a good student".format(name,age))

reg("mingyue",21)
reg("xiaojing",23,"female")

# 代码片段7
# 普通参数及调用法
def stu(name,age,addr):
    print("I am a student")
    print("我叫{0},我今年 {1} 岁了，我住{2}".format(name,age,addr))

n = "jingjing"
a = 18
addr = "大石坝"
stu(a,n,addr)  # 普通参数，只按照位置传递，容易出错
stu(name=n,age=a,addr=addr)  # 普通参数，只按照位置传递，容易出错
# 关键字参数及调用法
def stu_keyword(name="No name",age=0,addr="No addr"):
    print("我是个学生！")
    print("我叫{0},我今年{1}岁了，我家住在{2}".format(name,age,addr))

h = "大东"
b = 15
j = "观音桥"
stu_keyword(age=b,addr=j,name=h)

# 代码片段8
# 函数模拟一个学生进行自我介绍，但具体内容不清楚。把args看成一个列表
def stu(*args):
    print("Hello 大家好，我自我介绍一下，简单说两句：")
    print(type(args))
    for item in args:
        print(item)

stu("liuying",18,"重庆沙坪坝区","wangxiaojing","single")
stu("周大生")
stu()  # 收集参数可以不带任何参数调用，此时收集参数为空tuple
# stu(name="liuying")  # 如果使用关键字参数格式调用，会出现问题

# 代码片段9
# 自我介绍，调用的时候需要使用关键字参数调用
def stu(**kwargs):
    # 在函数体内对于kwargs的使用不用带星号
    print("Hello 大家好，很高兴认识大家，我先自我介绍一下：")
    print(type(kwargs))
    # 对于字典的访问，python2和python3有区别
    for k,v in kwargs.items():
        print(k,"------",v)

stu(name="小红",age=19,addr="重庆江北区",lover="王晓静",work="Teacher")
print("-------------")
print("+"*20)
stu(name="周大大大")
stu()  # 收集参数可以为空

# 代码片段10
def stu(name,age,*args,hobby="没有",**kwargs):
    print("Hi 大家好！！！")
    print("我叫{0},我今年{1}岁了。".format(name,age))
    if hobby == "没有":
        print("我没有爱好，很遗憾！")
    else:
        print("我的爱好是{0}".format(hobby))
    print("*"*20)
    for i in args:
        print(i)
    print("#"*30)
    # 字典用法请注意.items()
    for k,v in kwargs.items():
        print(k,"-----",v)

name = "小小明明"
age = 18
# 不同格式的调用
stu(name,age)
stu(name,age,hobby="游泳")
stu(name,age,"王晓静","刘小毛",hobby="游泳",hobby2="烹饪",hobby3="看书读报")

# 代码片段11
def stu(*args):
    print("hahhahaahhhh")
    n = 0  # n用来表示循环次数，主要用来调试
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)

# stu("小花花","大明明",19,200)
l = ["小胖胖",19,23,"李甜甜"]
stu(l)  # 此时，args的表示形式是字典内一个list类型的元素，即args=(["小胖胖",19,23,"李甜甜"],),很显然跟我们最初的想法违背
# 此时的调用，我们就需要解包符号，即调用的时候前面加一个星号
# 同理，dict类型收集参数一样可以解包，但是：对dict类型进行解包需要用两个星号进行解包
stu(*l)

# 代码片段12
def func_1():
    print("有返回值呀")
    return 1

def func_2():
    print("没有返回值")
    return "NONE"

f1 = func_1()
print(f1)
f2 = func_2()
print(f2)

# 代码片段13
# 文档案例，函数stu是模拟一个学生的自我介绍
def stu(name,age,*args):
    '''
    这是文档
    这是第二行
    这是文档第三行
    '''
    print("This is 函数 stu")

help(stu)
print(stu.__doc__)  # 外层不加print，没起作用？？

# 代码片段14
a1 = 100
def fun():
    print(a1)
    print("I am in fun")
    a2 = 99  # a2的作用范围是fun
    print(a2)

print(a1)
fun()
# print(a2)  # 不可以，a2作用域限制为局部变量，报错：a2 is not defined

# 代码片段15
# def fun():
#     global b1
#     b1 = 100
#     print(b1)
#     print("I am in fun")
#     b2 = 99  # b2的作用范围是fun
#     print(b2)
#
# print(b1)
# fun()
# 报错，b1 is not defined

def fun():
    global b1
    b1 = 100
    print(b1)
    print("我在函数里")
    b2 = 99  # b2的作用范围是fun
    print(b2)

fun()
# 为什么print（b1）出现在函数调用前面，则会报错？
print(b1)

# 代码片段16
a = 1
b = 2
def fun(c,d):
    e = 111
    print("局部变量={0}".format(locals()))
    print("全局变量={0}".format(globals()))

fun(100,200)

# 代码片段17
x = 100
y = 200
z1 = x + y
z2 = eval("x+y")
print(z1)
print(z2)

# 代码片段18
x = 3
y = 7
z1 = x + y
z2 = exec("x+y")
print(z1)
print(z2)

x = 8
y = 12
z1 = x + y
z2 = exec("print('x+y:',x+y)")
print(z1)
print(z2)

# 代码片段19
# 递归调用深度限制代码
# x = 0
# def fun():
#     global x
#     x += 1
#     print(x)
#     fun()  # 函数自己调用自己
#
# fun()

# 斐波那契数列
# 下面求斐波那契数列函数有一定问题，比如n一开始就是负数，如何修正？
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)  # 为什么此return能够正确执行而不用else语句

print(fib(3))
print(fib(10))

# 代码片段21
def hano(n,a,b,c):
    '''
    汉诺塔递归实现
    :param n: 代表几个盘子
    :param a: 代表第一个塔a，开始的塔
    :param b: 代表第二个塔b，中间过渡的塔
    :param c: 代表第三个塔c，目标塔
    :return: 输出移动顺序
    '''
    if n == 1:
        print(a,"---->",c)
        return None
    if n == 2:
        print(a,"---->",b)
        print(a,"---->",c)
        print(b,"---->",c)
        return None
    hano(n-1,a,c,b)  # 把n-1个盘子，从a塔借助于c塔，移到b塔上
    print(a,"---->",c)
    hano(n-1,b,a,c)  # 把n-1个盘子，从b塔借助于a塔，移到c塔

a = "A"
b = "B"
c = "C"
n = 3
hano(n,a,b,c)


