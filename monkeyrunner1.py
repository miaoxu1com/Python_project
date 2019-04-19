#coding:utf-8
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
import os

# cwd = os.getcwd()
# print(cwd)
os.system("clear")
os.chdir("C:\\Users\\Auser\\Desktop\\monkey\\")
try:
	os.remove("mypic.png")
except:
	pass

device_ = mr.waitForConnection()
# print(device_)
device_.removePackage('com.tal.kaoyan')

print("installing App....")
install_path = "C:\\Users\\Auser\\Desktop\\monkey\\"
apk_name = "kaoyanbang_3.3.6.242.apk"
file_path = install_path + apk_name
device_.installPackage(file_path)

print("launch App....")
pack_name = "com.tal.kaoyan"
activity_name = "com.tal.kaoyan.ui.activity.SplashActivity" 
pack_activity = pack_name + '/' + activity_name
# print(pack_activity)
device_.startActivity(pack_activity)
u = 1000
mr.sleep(4)

device_.touch(493,34,'DOWN_AND_UP')
mr.sleep(2)

print("input UserInfo.....")
device_.touch(100,186,'DOWN_AND_UP')
device_.type("miaoxu1com")
mr.sleep(2)
device_.touch(250,231,'DOWN_AND_UP')
device_.type("1012460248com")
mr.sleep(2)

print("longing....")
device_.touch(258,305,'DOWN_AND_UP')
mr.sleep(4)

print("cut pic.....")
# pic_name = 'mpic.png'
# pic_path = install_path + pic_name
# print(result,pic_name,install_path,pic_path)
# install_path+'mypic.png'

screenshot=device_.takeSnapshot()  
screenshot.writeToFile("C:\\Users\\Auser\\Desktop\\monkey\\mypic.png","png")
mr.sleep(2)