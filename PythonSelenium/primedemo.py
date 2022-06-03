

num=13
Flag=False

if num>1:
    for i in range(2,num+1):
        for j in range (2,i):
            if i % j==0:
                 Flag = True
                 break

        if Flag!=True:
            print(i," Prime")
        #else:
           # print(i,"prime")

        Flag=False

    #for i in range(2, num):
     #   print(i)