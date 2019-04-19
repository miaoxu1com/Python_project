#导入java类库
from com.andriod.monkeyrunner import MonkeyRunner as mr
from com.andriod.monkeyrunner import MonkeyDevice as md
from com.andriod.monkeyrunner import MonkeyImage as mi

#获取连接对象
device_ = mr.waitForConnection()
#安装App
print("installing App....")
install_path = r"C:\Users\Auser\Desktop\kaoyanbang_3.3.6.242.apk"
device_.installPackage(install_path)
#启动App
print("launch App....")
pack_name = "com.tal.kaoyan"
activity_name = "com.tal.kaoyan.ui.activity.SplashActivity" 
pack_activity = pack_name + '/' + activity_name
print(pack_activity)
device_.startActivity(pack_activity)
u = 1000
mr.sleep(4*u)
#取消按钮
device_.touch(493,34)
mr.sleep(2*u)
#输入用户信息
print("input UserInfo.....")
device_.touch(100,186)
device_.type("miaoxu1com")
mr.sleep(2*u)
device_.touch(250,231)
device_.type("1012460248com")
mr.sleep(2*u)
#点击登录
print("longing....")
device_.touch(258,305)
mr.sleep(4*u)
#截图
pic_path = ''
print("cut pic")
pic_data = mi.takeSnapShot()
pic_data.writeToFile()

#..
