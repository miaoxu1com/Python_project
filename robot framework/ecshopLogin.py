# coding=UTF-8
import time
from selenium.webdriver.support.select import Select
from ecshopLib import  pymysqlOperation as dbOperation
#conn = pymysql.connect(host="192.168.1.47", port=3306, user="root", passwd="111111", db="ecshop")
# sql = "select *from ecs_goods where goods_name='youtiao'"
#登录模块
sql = "select *from  ecs_admin_user"
dbopera = dbOperation()
result = dbopera.QueryData(sql)
driver = result[1]
result = result[0]
driver.find_element_by_name("username").send_keys(result[0][1])
driver.find_element_by_name("password").send_keys("caichang1")
driver.find_element_by_xpath("//input[@value='登 录']").click()
#添加商品模块
driver.switch_to_frame()