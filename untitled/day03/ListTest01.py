student = "张金山"
stuent =['张金山','蒋勋','刘志丛']# 建议类别中存储一种数据类型
student=[1,3,45,23,111111]
student=[True,True,True,False,False]
stuents =['张金山','蒋勋','刘志丛',1,2,3,True] #列表中可以存储多种数据类型，但是一般不建议这样

stuents =['张金山','蒋勋','刘梓崇',"刘德华",'郭富城']

#通过索引  得到元素
print(stuents[3])
print(stuents[1])

#通过索引修改元素
stuents[3] = "郭碧婷"
print("修改元素之后：",stuents)

# for

for value in stuents:
    print(value,end='-')

print("===============================")

#while
l01 = len(stuents)# 得到列表的长度
i = 0 # 表示索引 初始值 0
index_last = l01 -1 # 最后一个元素对的索引

while i <= index_last:
    print(stuents[i],end="-")
    i += 1

#  元素类型不统一，隐患
# stuents =["刘德华",'张金山',5,"刘德华",'蒋勋','刘梓崇',"刘德华",'郭富城'"刘德华"]
# str_sum = ''
# for stu  in stuents:
#     str_sum += stu
#
# print(str_sum)