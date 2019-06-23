#定义函数及异常处理：

# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(11))

#返回多个值：
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny









#异常处理
# #1：
# # try:
#     fh = open("testfile", "w")
#     # fh = open("testfile", "r")  #报异常，没有文件写权限
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print ("Error: 没有找到文件或读取文件失败")
# else:
#     print ("内容写入文件成功")
#     fh.close()
#
# #2：try-finally 语句无论是否发生异常都将执行最后的代码
# try:
#     fhh = open("testfile", "w")
#     fhh.write("这是一个测试文件，用于测试异常!!IIIII")
# finally:
#     print ("Error: 没有找到文件或读取文件失败")
#     fhh.close()
#
# #综合：
# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("这是一个测试文件，用于测试异常!!")
#     finally:
#         print "关闭文件"
#         fh.close()
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"

"""
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
    
=======================================================
    
try:
    正常的操作
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
    

try-finally 语句无论是否发生异常都将执行最后的代码：
try:# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument

# 调用函数
temp_convert("xyz");
    <语句>
finally:
    <语句>    #退出try时总会执行

"""

# 单个异常实例
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except (ValueError, ArithmeticError):
        print ("参数没有包含数字\n", ArithmeticError)

# 调用函数
temp_convert(222)


