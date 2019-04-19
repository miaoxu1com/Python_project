#coding: utf-8
#-*-utf-8-*-
#json处理库
import json
import re
import configparser
import time
#自动编码库
import codecs
#xml处理库
import xml.sax
import os
import logging
import types
#logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.INFO)
# type('abc') == str
# type(124) == types.FunctionType
#s = r'\n这只是\n' # 字符串中的“\n”只是字符，没有换行的意义了
#time.sleep(1)
'''
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
'''

# print(dir(logging))
# print(os.name)
# logging.info('报错信息')
# logging.info(isinstance(os.name,str))
#logging.info('logging 是否有这个属性或者方法:')
# logging.info('logging 是否有这个属性或者方法:%s' %hasattr(logging,'info'))
# logging.info(getattr(logging,'info'))

def OutInfo():
    print("================================")
    print("=       1.添加会员信息        =")
    print("=       2.显示会员信息        =")
    print("=       3.搜索会员信息        =")
    print("=       4.注册账号            =")
    print("=       5.登录账号            =")
    print("=       6.退出系统            =")
    print("================================")

def AddMemInfo():
    global MemInfo
    MemName = input("请输入会员姓名:\n")
    MemSex = input("请输入会员性别:\n")
    MemAge = input("请输入会员年龄:\n")
    if MemName in MemInfo.keys():
        MemName = input("会员姓名已存在请重新输入:\n")
#         MemInfo.update({
#             MemName: [MemName, MemSex, MemAge]
#         })
#         with open('Meminfo.json', 'a') as f:
#             print(json.dump(MemInfo,f,ensure_ascii=False,))
# #        f.write()
#     else:
    MemInfo.update({
        MemName:[MemName,MemSex,MemAge]
    })
    with open('Meminfo.json', 'a',encoding='utf-8',newline='\n') as f:
        print(json.dump(MemInfo,f, ensure_ascii=False,indent=4))
    print(MemInfo)

def DisplayMemInfo():
    if len(MemInfo) > 0:
        for i in MemInfo.keys():
          print("会员姓名\t会员的性别\t会员年龄")
          print(MemInfo.get(i)[0],"\t",MemInfo.get(i)[1],"\t",MemInfo.get(i)[2])
    else:
        print("请您先添加会员信息:")
        OutInfo()
        UserChois()

def SearchMemInfo():
    if len(MemInfo) > 0:
        MemName = input("请输入要搜索的会员姓名:")
        if MemName in MemInfo.keys():
           print("会员姓名是:",MemInfo[MemName][0],"\t会员性别是:\t",MemInfo[MemName][1],"\t会员的年龄是:\t",MemInfo[MemName][2])
        else:
           print("该会员信息不存在")
    else:
        print("请您先添加会员信息:")
        OutInfo()
        UserChois()
def ExitSystem():
    exit()
def UserChois():
    Opt = input("请输入1-4任意一个选项:\n")
    if Opt.isdigit():
        Opt = int(Opt)
        if Opt == 1:
            AddMemInfo()
            OutInfo()
            UserChois()
        elif Opt == 2:
            DisplayMemInfo()
            OutInfo()
            UserChois()
        elif Opt == 3:
            SearchMemInfo()
            OutInfo()
            UserChois()
        elif Opt == 4:
            userRegist()
        elif Opt == 5:
            userLogin()
        elif Opt == 6:
            ExitSystem()
        else:
            OutInfo()
            print("请重新输入1-4任意一个选项:\n")
            UserChois()
    else:
        print("输入错误,请重新输入1-4任意一个选项:\n")
def iniConfig():
    global config
    global list_data
    # global list_data
    # curpath = os.path.dirname(os.path.realpath(__file__))
    # cfgpath = os.path.join(curpath, "UserInfo.ini")
    # config.read(cfgpath, encoding="utf-8")
    # if config.has_section('UserInfo'):
    #     config.read("UserInfo.ini", encoding="utf-8")
    #     list_data = config.items("UserInfo")
    try:
        config.read("UserInfo.ini",encoding="utf-8")
    except:
        pass
    if config.has_section('UserInfo') == False:
        config.add_section('UserInfo')
        list_data = []
    else:
        list_data = config.items("UserInfo")

def userRegist():
    global config
    global list_data
    global username
    # print(len(config.sections()))
    # if(0):
    #     print("真")
    # else:
    #     print("假")
    # exit(0)
    # config.read('UserInfo.ini')
    username = input("请输入用户的名字：")
    password  = input("请输入用户的密码：")
    if config.has_option('UserInfo',username):
        if username in config.options('UserInfo'):
          print("用户名已经存在")
          username = input("请输入用户的名字：")
    else:
            # if re.match(r'^(.*[a-z][A-Z])(.*[0-9]{4,})$',userName) and re.match(r'^(.*[a-z][A-Z])(.*[0-9]{6,})$',userPassword):
            print("注册成功，现在可以登录了！")
            # print(config.sections())
            # config.read('UserInfo.ini')
            # config.sections()
            #config.add_section('Section1')
            # if config.has_section('UserInfo'):
            # print(config.has_section('UserInfo'))
            # config.read("UserInfo.ini", encoding="utf-8")
            # list_data = config.items("UserInfo")
            # print(list_data)
            # print(list(list_data))
            # print(type(list_data) is list)
            print((username,password))
            list_data.append((username,password))
            for i in list_data:
                config.set('UserInfo',i[0],i[1])
            # else:
            # config.set('UserInfo', username, password)
            # if len(config.sections()) == 0:
            #     print("1")
            #     config.add_section('UserInfo')
            #     config.set("UserInfo", userName, userPassword)
            # else:
            #     config.set("UserInfo", userName, userPassword)
            #     config.set("UserInfo", userName, userPassword)
            # else:
            # userInfo = {userName:userPassword}
            config.write(open("UserInfo.ini",'w',encoding="utf-8"))
            # else:
            # print("密码或用户名含有非法字符如：&等")
            # userRegist()
    OutInfo()

def userLogin():
    pass
    # userName = input("请输入用户的名字：")
    # userPassword = input("请输入用户的密码：")
    # config = configparser.ConfigParser()
    # config.sections()
    # config.read('./Config/UserInfo.conf')
    # print(config.items('UserInfo'))
    # if userName == config.items('UserInfo'):


list_data = None
config = configparser.RawConfigParser()
# print(dir(config))
# exit()
MemInfo = dict();
OutInfo()
iniConfig()
userRegist()
# UserChois()
# a = {'zhangsan':'nan'}
# a = {'lisi':'k'}
# print(len(a))
#密码校验
'''
校验密码是否合法
def check_password(passwd):
    if re.match(r'^(?=.*[A-Za-z])(?=.*[0-9])\w{6,}$',passwd):
        print "password %s correct"%passwd
        return True
    else:
        print "password %s is invalid"%passwd
        return False
        
rightname="skykylin"
rightpsw="123"
输入计次
id=0
while 1：
    name=input("请输入用户名")
    psw=input("请输入密码")
    if name==rightname and psw==right:
        print("你登录成功了")
        exit(0)
    else：
        if id<2：
            print("请重新输入")
            id=id+1
        elif id==2：
            print("你错的有点多哦")
            exit(O)
'''