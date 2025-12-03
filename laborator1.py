'''s = float(input("s (lei):"))
p = float(input(" p (% per year):"))
interest = s*p /400.0
print("начисленный процент за 3 месяца:", interest)'''


'''#9
import math
s = float(input("s (площадь):"))
if s < 0:
    print("ошибка: площадь не может быть отриуательной .")
else:
    a = math.sqrt(s)
    perim = 4* a
    print("сторона :", a)
    print("периметр :",perim)'''

#13
x = int(input("размер файла X (кб): "))
y = int(input("размер файла y (кб): "))
z = int(input("размер файла z (кб): "))
disk = 1440
total= x + y + z
if total % disk == 0:
    disks = total // disk
else:
 disks = total // disk + 1 
print ( "нужно дискет :" , disks )

