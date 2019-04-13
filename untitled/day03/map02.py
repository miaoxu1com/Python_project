map_ ={"name01":"张三01",
       "name02":"张三02",
       "name03":True,
       "name04":"张三05",
       "name05":4,
       "name06":"张三06",
       "name07":"张三07"}


#  得到所有key值组成的列表
keys = map_.keys()
print(keys)


#  直接获取说有的 key：value
for key  in keys:
    print(key,map_.get(key))


print("==================================")

# 得到所有的value值组成的类别   不多
values = map_.values()
print(values)


print("==================================")

# 得到所有的 键值对列表
k_v_s = map_.items()
print(k_v_s)



#  直接获取说有的 key：value
for key,value  in map_.items():
    print(key,value)
