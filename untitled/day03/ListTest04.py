#删除

my_list = [10,20,40,30,40,50,60,70,40,40,67]

#根据值来删除  remove
my_list.remove(40)
print(my_list)

#根据索引删除, 使用 pop 方法,
my_list.pop(6)
my_list.pop(6)

print(my_list)

#该方法不传递索引时默认删除最后一个元素,
my_list = [10,20,30,40,50,60,70,40]
my_list.pop()
print(my_list)


#my_list = [10,20,40,30,40,50,60,70,40,40,67] 删除其中所有的40元素
