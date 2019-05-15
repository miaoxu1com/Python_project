#coding=utf-8
#读取就是get获取配置信息的意思
#为了方便快速的单独配置每一项所以针对不同的操作建立不同
#配置文件
import ConfigParser
import os
import codecs
import chardet
#对操作配置文件的方法进行封装
class readConfig():
    #定义为属性只需要执行一次，定义为init每次都要执行
    cf =  ConfigParser.ConfigParser()
    cf_dirname = os.path.dirname(os.path.realpath("config.ini"))
    cf_path = os.path.join(cf_dirname,"config.ini")
    #这里的读对下面的影响吗，下面永远是rb
    cf.read(cf_path)

    def __init__(self):
        # print(self.cf_path)
        #open打开
        # fd = codecs.open(self.cf_path)
        # print(fd)
        # print(fd)
        # print("-------------")
        # data = fd.read()
        # print(data)
        pass
        #remove BOM
        # print(data[:3],codecs.BOM_UTF8)
        # if data[:3] != codecs.BOM_UTF8:
        #     data = data[3:]
        #     #codecs.open打开
        #     file = codecs.open(self.cf_path,'w')
        #     file2 = codecs.open(self.cf_path,'w')
        #     # datafile = file.read()
        #     # print(file,file2)
        #     # print("-------------")

        #     # file.write(data)
        #     file.close()
        # fd.close
        #在这里测试可以写所以应该是上面config的读在没有关闭
        #操作之前只能是rb模式
        # fd = codecs.open(self.cf_path,'w')
        # print(fd)
        # print(data)

    def get_http(self,section,option):
       value = self.cf.get(section,option)
       return value
    def get_email(self):
        print("email")
    def get_database(self):
        print("database")
readcf = readConfig()
http_url = readcf.get_http('HTTP','baseurl')
# print(http_url)
# a = "你好啊"
# b =b"abcd"
# c = "你好烦活动费fhdskfhlsd"
# d ="你好烦活动费fhdskfhlsd"
# e = "你好烦活动费fhdskfhlsd"
# print(chardet.detect(a),chardet.detect(b),chardet.detect(c),chardet.detect(d),chardet.detect(e))
# print(type(a),type(b),type(c),type(d),type(e))
# print("a:"a,"b:",b,"c:",c,"d:",d,"e:",e)
# print(a)