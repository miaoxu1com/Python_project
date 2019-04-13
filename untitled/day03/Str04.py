# 替换字符串中的元素 replace函数，有返回值 返回替换之后的新的字符串 工--->人
str01="SDSDF手工对方公司法工规的故工事是法国"
str01 = str01.replace("工","人") # 不写第三个参数  替换所有
print(str01)

str01 = str01.replace("人","工",1) #第三个参数   数字是几就替换几个
print(str01)

str01 = str01.replace("人","工",2)
print(str01)

# str01 = str01.replace("工","人",2)
# print(str01)




