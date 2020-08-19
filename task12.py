spisok = [4,6,10,9,3,1]
la = list(map(lambda x : True if not x % 2 else False,spisok))
print(la)