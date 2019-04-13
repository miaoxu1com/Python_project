tour = []  # 这个列表 存储了 所有的 落下来 和 升上去的距离   ----》目的为了得到 路程
height = []  # 这个列存储了  所有的升上去的距离，   -----》为了得到第10次升上去的距离

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)

    hei /= 2

    height.append(hei)

# print('总高度：tour = {0}'.format(sum(tour)))
# print('第10次反弹高度：height = {0}'.format(height[-1]))

print("tour列表：",tour)
print("height列表：",height)

print('总高度：tour = ',sum(tour))
print('第10次反弹高度：height = ',height[len(height)-1])