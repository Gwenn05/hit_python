name = input('nhap ten : ').split()
for i in name : 
    i = i[0:1].upper() + i[1:].lower()
    print(i, sep=' ', end=' ')