spisok = [4,6,5,10,9,3,1]
la = list(map(lambda x : "четный" if not x % 2   else "нечетный",spisok))
print('Четные',la.count("четный"),'\nнечетные', la.count("нечетный"))