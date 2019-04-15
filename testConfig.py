#coding:utf-8
import  configparser
import os
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "cfg.ini")
print(cfgpath)  # cfg.ini的路径

# 创建管理对象
conf = configparser.ConfigParser()

# 读ini文件
conf.read(cfgpath, encoding="utf-8")  # python3
# 获取所有的section
sections = conf.sections()
# conf.add_section("emali_tel")
conf.set("emali_tel", "e", "yoyo1@tel.com")
conf.set("emali_tel", "f", "265")
conf.set("emali_tel", "a", "265")
conf.set("emali_tel", "b", "265")
conf.set("emali_tel", "c", "265")
print(sections)  # 返回list
with open(cfgpath,"w") as f:
    conf.write(f)