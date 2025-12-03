'''#7
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
if c < d:
 result = a + b
 print("c < d ,сумма a + b =" , result)
else:
 result = c * d
 print("c >= d , произведение c * d =", result)'''


'''#8
s = float(input ("растояние s (км) = "))
v1 = float(input ("скорость v1 (км/ч) = "))
v2 = float(input ("скорость  v2 (км/ч) = "))
if v1 + v2 == 0:
    print("обе скорости нулевые - они не встретяться.")
else:
    t = s / (v1 + v2)
    print(" время до встречи ( в часах):" ,t )'''


#14
import math
A = float(input( " A = "))
B = float(input( " B = "))
C = float(input( " C = "))
if A  == 0:
 print(" A не должен быть 0 -это не квадратное уравнение .")
else:
  D = B*B -4*A*C
  print("дискременант  D=", D )
  if D > 0:
    x1 = (-B + math.sqrt(D))/(2*A)
    x2 = (-B + math.sqrt(D))/(2*A)
    print("два корня :x1=",x1,"и x2",x2)
  elif D == 0:
    x = -B / (2*A)
    print(" один корень (двукратный ): x=", x)
  else:
    print("действительных корней нет (D < 0).")

    
    
