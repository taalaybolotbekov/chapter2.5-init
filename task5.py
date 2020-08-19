num = lambda x , y : x in y
xy =[1,2,4]
yx =[3,2,1]
lis = [num(i,yx) for i in xy]
lis1 = [num(i,xy) for i in yx]
print(lis,lis1,f'{xy},{yx}')