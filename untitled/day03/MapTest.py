# 列表
list_ = ["张三01","张三02","张三03","张三04","张三05","张三06","张三07"]

# 字典   key:value 键值对      hashcode
'''
key 是唯一的 并且通常为字符串
value 可以重复，可以是任意数据类型

'''
map_ ={"name01":"张三01",
       "name02":"张三02",
       "name03":True,
       "name04":"张三05",
       "name05":4,
       "name06":"张三06",
       "name07":"张三07"}


# 通过key  得到 value

# 若需要得到 张三05 必须知道其key   字典对象[key]，这种方式不好 若key不存在，则会报错
value04 = map_["name04"]
print(value04)

#
# value04 = map_["name00"]
# print(value04)

# 通过key得到value 另一种方式  get，总是key不存在 也不会报错. 更加健壮
vavlue06 = map_.get("name00")
print(vavlue06)

# 添加元素  和  修改元素

# 若key存在  就是修改
map_["name03"] = "郭碧婷"

print(map_)

# 若key不存在  就是添加元素
map_["name08"] = "翠花"

print(map_)

#  删除  根据key来删除
map_.pop("name03")
print(map_)

# 清空 容器中的所有的数据
map_.clear()
print(map_)