# coding=UTF-8
from selenium import  webdriver
import pymysql
class pymysqlOperation():
    def QueryData(self,sql):
        driver = webdriver.Chrome("C:\Users\Auser\Desktop\ChromePortable_2\Chrome.72.0.3626.121.x64\chromedriver.exe")
        driver.get("http://192.168.1.47/ecshop/admin/")
        # 连接数据库
        conn = pymysql.connect(host='192.168.1.47', user='root',password='111111', database='ecshop', port=3306,charset='utf8')
        cs = conn.cursor()
        cs.execute(sql)
        result = cs.fetchall()
        return [result,driver];
