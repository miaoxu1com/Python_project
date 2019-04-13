"""
index 方法可以根据值查找, 查找到返回该值元素所在的位置, 查找失败会报错, 程序终止. 我们可以先使用 count 方法可以统计值出现的次数, 如果不为0, 再使用 index 方法.
Count(x)  查找某个列表中x有多少个
Index(x) 查找某个元素x的索引是多少

"""
# 将列表中的 40 都改成 100
my_list = [10,20,30,40,50,60,70,40,40,67]
#30 2     my_list[2]
# 40 3
# 50  4  my_list[4]


# print(my_list.count(23))  在列表中  查找元素有多少个
# if my_list.count(40) > 0:
#     posi_first = my_list.index(40)
#     print(posi_first)
#     # my_list[posi_first] = 100
#
#     posi_sec = my_list.index(40,posi_first+1)
#     print(posi_sec)
    # my_list[posi_first] = 100


print("===================")
# 判断列表中是否有  40 元素，若有  将所有替换为  100

if my_list.count(40) > 0:

   # index_ = my_list.index(40)
    num_index = -1# 临时存储上一个 索引，初始值为0
    for ele in my_list:
       if ele == 40:
           index_ = my_list.index(ele,num_index+1)
           num_index =index_
           # print(index_)
           my_list[index_] = 100

    # i = 0
    # while i <= len(my_list)-1:
    #     if my_list[i] == 40 :
    #         my_list[i] = 100


else:
    print("没有40")


print("修改之后的新的列表：",my_list)

