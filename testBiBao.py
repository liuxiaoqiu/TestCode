#! /usr/bin/env python
# coding=utf-8
# http://***

#定义一个函数
def plus(number):
    #在函数内部再定义一个函数，其实这个里面的函数就被认为是闭包
    def plus_in(number_in):
    #这里打印一下number_in变量，以便大家可以更清楚传进来的变量时哪一个
        print str(number_in) + "\r\n"
        return number+number_in
    #其实这里返回的就是闭包的结果
    return plus_in


#给plus函数赋值，这个20就是给参数number
v1=plus(20)

#注意这里的100其实给参数number_in

print v1(100)