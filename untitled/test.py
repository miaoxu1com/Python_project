#example1
#print("Hello World");
# n1=9
# n2=4
# n3=5
# cm1 = 1000
# cm2 = 2000
# mm1 = cm1*1000
# mm2 = cm2*2000
# print("n1+n2+n3",(n1+n2+n3,mm1,mm2));
#example2
# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 30
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven*space_in_a_car
# average_passeners_per_car = passengers / cars_driven
# print ("there are",cars,"cars avaiable")
# print ("there are only",drivers,"drivers available")
# print ("there will be ",cars_not_driven,"empty cars today")
# print ("we can transport",carpool_capacity,"pople today")
# print ("we have",passengers,"to carpool today")
# print ("we need to put about",average_passeners_per_car,"in each car")
# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
# print ("Here's your file %r:" %filename)
# print (txt.read())
#
# print ("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
#
# print (txt_again.read())
#from sys import argv
# if 2==1:
#     print("zhen");
# else:
#     print("jia");
#元组 列表数据类型
'''
t = ('java','python','php',['a','b']);
length = len(t)-1;
t[length][0] = 'x';
t[length].append('z');
t[length].pop(2)
t[length].insert(1,'f');
print (type(t),t[0],t[length][0]);
print(len(t[length]),t[length]);
'''
#input的一次输入多个值中间需要使用逗号分割
#a,b=input("加数1:加数2:").split();
# print(a,b,a+b);
'''
简单运算符
比较运算符的适用范围  左右两边的数据类型要相同返回true，否则false
1.== 判断左右两边的操作数数值和数据类型是否相等 若相等返回 true 否则返回false
2.!=
https://www.cnblogs.com/jiyongjia/p/9539024.html
3.<=  >、<、> = 、< =、比较的规则为：从第一个字符开始比较，排序在前边的字母为小，当一个字符串全部字符和另一个字符
串的前部分字符相同时，长度长的字符串为大。
4.>=
5.<
6.>
'''
'''
a=7<5;
b=7>=5;
c=8<=7;
print(a,b,c);
复合运算符
not and or
if分支语句
if 条件:
else:
if 条件1：
elif 条件2:
elif 条件3:
else:
if 3>5:
    print("成立");
else:
    print("不成立");
    if 1 and 9 and 0:
    print("成功")
else:
    print("不成功")
if not 0 or 1:
    print("成功")
else:
    print("不成功")
    查看是方法还是  函数 
    input()函数 .split()方法  可以使用find usage来查看是方法还是函数  goto 去定位到函数或者方法所在的文件夹
print(len('中'.encode('utf-8')))
print('中'.encode('utf-8'))
'''
'''
user,password = input("请输入用户名和密码:").split()
if user == "狗剩" and password == "123456":
    print("登录成功")
else:
    print("用户或者密码错误")
 '''
import random,keyword
# print(keyword.kwlist);
#user = int(input("请输入一个整数:"));
'''
while True:
    user = input("请输入一个整数:")
    if user.isdigit() and int(user) in list(range(0,3)):
        user = int(user);
        com = random.randint(0,2);
        userdic = {'user':user}
        com = {'com':com}
        print("数字:",userdic['user'],type(userdic['user']),"\n的数字:",com['com'],type(com['com']))
        if userdic['user'] == 0 and com['com'] ==1:
            print("恭喜你赢了");
        elif userdic['user']  == 1 and com['com']== 2:
            print("恭喜你赢了");
        elif userdic['user']  == 2 and com['com']== 0:
            print("恭喜你赢了");
        elif userdic['user']  == com['com']:
            print("本局平局");
        else:
            print("电脑赢了");
    elif user in ['q','Q']:
        exit()
    else:
        print('输入错误请重新输入')
        continue;
'''
'''
循环
1.初始化变量 i=0
2.循环条件 i<=4
3.循环迭代语句 i +=1
'''
"""
i = 1;
sum = 0;
while i<=100:
    if i%2==0:
        sum = sum + i;
    i +=1;
print(sum);
"""
"""
a = 1;
b = 2;
c = 3;
if a>0 and b>0 \
    and c>0 \
    and   8>1:
    {
        print("正确")
    }1
else:
    {
        print("失败")
    }
"""
'''
i = 3;
while i<9:
    print(i)
    i += 1;
for  i in range(3,9):
    print(i)
 '''
# print(sum(range(1,101)),'7897'.isdigit())

# 循环练习题
# 1.本金10000 元存入银行，年利率是千分之三。每过一年，将本金和利息相加作为新的本金。计算五年后，获得的本金是多少。
# i=1
# Principa = 10000
# while i<5:
#     Interest = Principa * 0.003
#     Principa = Principa + Interest
#     i+=1
# print(Principa)
# # 2.计算1000以内所有不能被7整除的整数的和
# sum = 0;
# for i in range(0,1001):
#     if(i%7 != 0):
#         sum = sum + i;
# print(sum);
# 3.编写一个程序，最多接受10 个数字，并求出其中所有正数的和。用户可通过输入999终止程序，
# 统计用户输入的正数个数，并显示这些正数的和
# sum = 0;
# numTotal = 0;
# positive = 0;
# while numTotal < 10:
#    num = input("请依次输入十个数字:");
#    if num.lstrip("-").isdigit():
#        numTotal += 1;
#        if int(num) > 0:
#         positive +=1;
#         sum += int(num);
# print("正数的和为:",sum,"\n正数的个数为:",positive);
# 4.开发一个标题为“FlipFlop”的游戏应用程序。它从1计数到100，遇到3的倍数就替换为单词“Flip”，
# 5的倍数就替换为单词“Flop”，既为3的倍数又为5的倍数则替换为单词“FlipFlop”。
# for i in range(1,101):
#     if(i%3==0):
#         i="Flip"
#     elif(i%5==0):
#         i="Flop"
#     elif(i%3==0 and i%5==0):
#         i="FlipFlop"
#     else:
#         continue
# 5.在控制台输出一个用‘*’组成的直角三角形
# print("*")
# print("*\t*")
# print("***********")
#替换指定的字符
# stru="人工附加分开的工发的是会计法工"
# c=0;
# ind = 0;
# for i in stru:
#     if  i=="工":
#         c+=1;
#         j=ind;
#         if c==2:
#             break
#     ind += 1;
# print(stru);
# newList = list(stru);
# newList[j]='';
# newstru=''.join(newList);
# print(newstru)


'''
stri = input("请输入一个字符:")
i = 0
isStr=0;
isNotNum = 0;
isSpace = 0;
isEl=0;
for i in stri:
    if(i.isdigit()):
        isStr += 1;
    if(i.isspace()):
        isSpace += 1;
    if(i.isalpha()):
        isNotNum += 1;
    else:
        isEl += 1;
print("是数字的:",isStr,"\n是字母或者汉字的:",isNotNum,"\n是空格的:",isSpace,"\n是特殊字符和空格和数字:",isEl);
'''
#作业第五题打印直角三角形
# i = 0
# while i < 5:
#     i+=1
#     print(i*"*");
#使用索引替换指定的值
# numList = [20,30,40,70,80,90,40,68,40,100];
# findNum = 40;
# if(numList.count(findNum)>0):
#     firstPos = numList.index(findNum);
#     numList[firstPos] = 100;
# for i in numList:
#     if (numList.count(findNum) > 0):
#        firstPos = numList.index(findNum,firstPos+1);
#        numList[firstPos] = 100
# print(numList);
# numList = [20,30,40,70,80,90,40,68,40,100];
# findNum = 40;
# i = 0
# listLen = len(numList);
# while i < listLen:
#     if numList.count(findNum)>0:
#         if numList[i] == 40:
#             numList.pop(i)
#     i +=1
# print(numList)
# numList = [20,30,40,70,80,90,40,68,40,100,40,40];
# print("删除之前",numList);
# for j in numList:
#     print(j);
#     if j == 40:
        #print(j);
        #删除值
        # numList.remove(j);
        #删除的是j这个变量，不是删除的numList的元素，list结构特点每删除一个列表的长度都在发生变化
        #del j
        # del numList[numList.index(j)]
        #删除列表索引的元素
        # print(numList.index(j));
        # numList.pop(numList.index(j))

# print("删除之后",numList);
heigh = [];
tenHeigh = [];
tempH=100;
for i in range(1,11):
    if i == 1:
        heigh.append(tempH)
    else:
        heigh.append(tempH*2)
    tempH /= 2;
tenHeigh.append(tempH);
print(tenHeigh,heigh);
print("第十次经过的路程",sum(heigh),"十次反弹的高度",tenHeigh[len(tenHeigh)-1]);

# dicV = {
#     'name1':'a',
#     'name2': 'b',
#     'name3': 'c',
#     'name4': '中国',
#     'name5': '1'
#
# }
# dicVK = dicV.keys();
# for key in dicVK:
#     print(key,dicV.get(key));

def str_count(stru):
    isStr = 0;
    isNotNum = 0;
    isSpace = 0;
    isEl = 0;
    for i in stru:
        if (i.isdigit()):
            isStr += 1;
        if (i.isspace()):
            isSpace += 1;
        if (i.isalpha()):
            isNotNum += 1;
        else:
            isEl += 1;
    print("是数字的:", isStr, "\n是字母或者汉字的:", isNotNum,
          "\n是空格的:", isSpace, "\n是特殊字符和空格和数字:", isEl);
    return stru

stri = input("请输入任何字符串:");


























