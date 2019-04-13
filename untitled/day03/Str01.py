# 遍历（循环） 出字符串中的每一个元素
str01 = "大发放而非asdfasfasdfa，，，，aadfa阿斯顿发水电费&&"


# ----->字符串中的元素都是有索引的，根据索引可以得到对应的元素
#  而---3
a = str01[3]
print(str01[3])

#  发---1
print(str01[1])

#---->计算字符串的长度
# 这个字符串中 有 35个元素 ，长度是35
l01 = len(str01)
print(l01)



str01 = "大放而非asdfasfasdfa，，，，aadfa阿斯顿发水电费&&"
# 最后一个元素的索引：字符串的长度-1

len01 = len(str01)# 字符串的长度
index_last = len01 - 1  # 最后一个元素的索引
i = 0 # i变量表示是  元素的索引

while i <= index_last:
    print(str01[i])
    i += 1

print()
print("上面的循环结束了 执行到这里")


'''
 0 1 2 .....  34
 

'''
