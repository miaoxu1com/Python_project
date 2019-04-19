#自己写的方法
def maopao():
	i = 0
	arr =[10,2,9,7,4,5,6,7,4,3,5,2]
	while i < len(arr)-1:
		j = 0
		while j < i+1:
			#不管怎么操作都是操作的原数组 所以直接  arr[] i j
			if ( arr[i] < arr[i+1] ):  #条件这里看是最大还是最小  结合状态栏
				#先保存被替换的  然后把新的值覆盖旧的值
				t = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = t
			j += 1
		i += 1
	print(arr)
maopao()
#参考网络的方法
my_list = [1,2,3,4,5,55,32,56,22,554,435,4353,3123,77]
count = len(my_list)
for i in range(0,count):
	for j in range(i+1,count):
		if my_list[j] > my_list[i]:
			my_list[i],my_list[j] = my_list[j],my_list[i]
print(my_list)
			
			