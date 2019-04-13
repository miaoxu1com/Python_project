l_=[10,20,30,40,50,40,40,40,40]

while l_.count(40)>0:
    i=0
    while i<len(l_):
        print(l_[i])
        if l_[i]==40:
           l_.pop(i)
        i+=1

print(l_)
