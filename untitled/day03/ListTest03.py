# 向列表中插入数据

my_list = [10,20,30,40,50]
print(my_list)

new_value = 12

# 将元素添加到末尾 append
my_list.append(new_value)
print(my_list)

#向指定索引位置插入元素
my_list.insert(2,new_value)
print(my_list)

# 将一个列表添加到另外一个列表的末位
new_li = [101,110]
my_list.extend(new_li)
print(my_list)