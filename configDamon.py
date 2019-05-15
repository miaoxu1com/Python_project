#print("hello word")
#Python 2.7.15
import logging
import os
import ConfigParser

# read config_file
#初始化config对象
config =  ConfigParser.ConfigParser()
#获取配置文件的路径
config_dir = os.path.dirname(os.path.realpath(__file__))
#拼接配置文件
config_path = os.path.join(config_dir,"config.ini")
#读取配置文件
config.read(config_path)
#print(config.sections())
#print(config_path)
#print(config.has_section("HTTP"))
#注意：首先在本次的编写代码中我又有了深刻的理解在if外边定义的变量
#相对于if来说就是一个全局的变量  当你在if里边操作时 再次在if外边打印
#系统不知道你要打印的是全局变量还是局部变量所以会报错，所以如果你想
#打印出来看一下结果 就要在if里边打印 for循环也一样
#判断是否存在HTTP节点
if config.has_section("HTTP"):
	#读取配置文件
    config.read(config_path)
    #获取节点信息
    http_data = config.items("HTTP")
    for val in http_data:
    	#打印节点项
    	print(val[0])
    #重新赋值节点项的值
    config.set("HTTP","baseurl","www.baidu.com")
    #更新节点项的值
    config.write(open(config_path,'w'))
    #重新打印节点项
    print(http_data)
else:
	#不存在该节点就添加节点
    config.add_section("HTTP")
    #判断节点是否添加成功
    if config.add_section("HTTP"):
    	#打印添加节点的交互信息
        print("add is success")
    else:
    	#打印添加节点的交互信息
        print("add is fail")

