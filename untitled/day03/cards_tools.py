card_list = []


def show_menu():
    """显示菜单"""
    print('*' * 50)
    print('欢迎使用【会员管理系统】')
    print('')
    print('1.新增会员')
    print('2.显示全部')
    print('3.搜索会员')
    print('0.退出系统')
    print('*' * 50)


def new_card():
    """新增名片"""
    print('-' * 50)
    print('新增会员')
    # 1.提示用户输入名片的详细信息
    name_str = input('请输入姓名：')
    phone_str = input('请输入电话：')
    qq_str = input('请输入QQ：')
    email_str = input('请输入邮箱：')

    # 2.使用用户输入的信息建立一个会员字典
    card_dict = {'name_str': name_str,
                 'phone_str': phone_str,
                 'qq_str': qq_str,
                 'email_str': email_str}

    # 3.将会员字典添加到列表中
    card_list.append(card_dict)  # 把一个字典追加到一个列表中
    print(card_list)
    # 4.提示用户添加成功
    print('添加%s的会员成功' % name_str)


def show_all():
    """显示所有名片"""
    print('-' * 50)
    print('显示所有会员')

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print('当前没有任何的会员记录，请使用新增功能添加会员')
        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不返回任何结果
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name,)
    print('')
    # 打印分隔线
    print('=' * 50)

    # 遍历会员列表依次输出字典信息
    for card_dict in card_list:
        # print card_dict
        print('%s\t\t%s\t\t%s\t\t%s' % (card_dict['name_str'],
                                        card_dict['phone_str'],
                                        card_dict['qq_str'],
                                        card_dict['email_str']))


def search_card():
    """搜索会员"""
    print('-' * 50)
    print('搜索会员')

    # 1.提示用户输入要搜索的姓名
    find_name = input('请输入要搜索的姓名：')
    # 2.遍历会员列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict['name_str'] == find_name:
            print('姓名 电话 QQ 邮箱')
            print('=' * 50)
            print('%s %s %s %s' % (card_dict['name_str'],
                                   card_dict['phone_str'],
                                   card_dict['qq_str'],
                                   card_dict['email_str']))

            # TODO 针对找到的会员记录执行修改和删除的操作
            # 在我们的日常编写程序中，如果一个函数的代码太多，阅读和编写都是一件困难的事情，而在开发中，可以针对一个具体独立的功能来封装一个函数，由这个函数来处理具体的操作，这样就能保证每个函数中的代码清晰明了，功能明确
            deal_card(card_dict)
            break

        else:
            print('抱歉，没有找到%s' % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input('请选择要执行的操作 '
                           '[1] 修改 [2] 删除 :')
    # 替换已经存在的键值对
    if action_str == '1':
        find_dict['name_str'] = input_card_info(find_dict['name_str'], '姓名：')
        find_dict['phone_str'] = input_card_info(find_dict['phone_str'], '电话：')
        find_dict['qq_str'] = input_card_info(find_dict['qq_str'], 'QQ：')
        find_dict['email_str'] = input_card_info(find_dict['email_str'], '邮箱：')

        print('修改会员成功！！！')
    elif action_str == '2':

        card_list.remove(find_dict)

        print('删除会员成功！！！')

def input_card_info(dict_value, tip_message):


    """

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，负责返回字典中原有的值
    """
    # 1.提示用户输入内容

    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回‘字典中原有的值’
    else:
        return dict_value


    # ============================================
# def a():
if __name__ == '__main__':  #  主函数  程序的入口
    # 无限循环，由用户主动决定什么时候退出
    while True:
        # TODO注释，用于标记需要去做的工作

        show_menu()

        action_str = input("请选择希望执行的操作: ")
        print("你选择的操作是 %s" % action_str)
        # 1,2,3针对名片的操作
        if action_str in ["1", "2", "3"]:
            if action_str == "1":
                new_card()
            elif action_str == "2":
                show_all()
            elif action_str == "3":
               search_card()

        # 0退出系统
        elif action_str == "0":
            print("欢迎再次使用【会员管理系统】:")

            break
            # 如果在开发程序时，不希望立刻编写分支内部的代码
            # 可以使用pass关键字，表示一个占位符，能够保证程序的代码结构正确
            # 运行程序时，pass关键字不会执行任何操作
        else:
            print("输入错误，请重新输入:")



# a()