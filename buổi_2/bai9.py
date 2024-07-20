# a
a = int(input('nhap a : '))
dem = 0
while a != 0 : 
    a //= 2
    dem += 1
print (dem)
# b
x = 'awesome'
print ('Python is', x)
print ('Python is {}'.format(x))
print(f'Python is {x}')
# c
import sys
print (sys.version)