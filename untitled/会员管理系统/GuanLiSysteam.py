def OutInfo():
    print("================================")
    print("=       1.添加会员信息        =")
    print("=       2.显示会员信息        =")
    print("=       3.搜索会员信息        =")
    print("=       4.退出操作系统        =")
    print("================================")

def AddMemInfo():
    global MemInfo
    MemName = input("请输入会员姓名:\n")
    MemSex = input("请输入会员性别:\n")
    MemAge = input("请输入会员年龄:\n")
    if MemName in MemInfo.keys():
        MemName = input("会员姓名已存在请重新输入:\n")
        MemInfo.update({
            MemName: [MemName, MemSex, MemAge]
        })
    else:
        MemInfo.update({
            MemName:[MemName,MemSex,MemAge]
        })
    print(MemInfo)

def DisplayMemInfo():
    if len(MemInfo) > 0:
        for i in MemInfo.keys():
          print("会员姓名\t会员的性别\t会员年龄");
          print(MemInfo.get(i)[0],"\t",MemInfo.get(i)[1],"\t",MemInfo.get(i)[2])
    else:
        print("请您先添加会员信息:")
        OutInfo()
        UserChois()

def SearchMemInfo():
    if len(MemInfo) > 0:
        MemName = input("请输入要搜索的会员姓名:")
        if MemName in MemInfo.keys():
           print("会员姓名是:",MemInfo[MemName][0],"\t会员性别是:\t",MemInfo[MemName][1],"\t会员的年龄是:\t",MemInfo[MemName][2])
        else:
           print("该会员信息不存在")
    else:
        print("请您先添加会员信息:")
        OutInfo()
        UserChois()
def ExitSystem():
    exit()
def UserChois():
    Opt = input("请输入1-4任意一个选项:\n")
    if Opt.isdigit():
        Opt = int(Opt)
        if Opt == 1:
            AddMemInfo()
            OutInfo()
            UserChois()
        elif Opt == 2:
            DisplayMemInfo()
            OutInfo()
            UserChois()
        elif Opt == 3:
            SearchMemInfo()
            OutInfo()
            UserChois()
        elif Opt == 4:
            ExitSystem()
        else:
            OutInfo()
            print("请重新输入1-4任意一个选项:\n")
            UserChois()
    else:
        print("输入错误,请重新输入1-4任意一个选项:\n")

MemInfo = dict();
OutInfo()
UserChois()
# a = {'zhangsan':'nan'}
# a = {'lisi':'k'}
# print(len(a))

