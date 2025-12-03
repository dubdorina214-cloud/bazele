'''#7
n = int(input("введите число n :"))
s = 0 
temp = n
while temp > 0:
 s += temp % 10
 temp   //=  10
 if  n % s == 0 :
  print("число делиться на сумму своих цыфр.")
 else:
  print("число не делиться на сумму своиц цыфр .")'''

#12
N = int(input("введите N "))
for i in range(N -1,-1,-1):
 print(i)

 '''#15
N = int(input("введите N:"))
for num in range(1, N +1):
  s = 0
  t = num 
  while t > 0 :
   s += t % 10 
   t //= 10 
   if s % 2 == 1:
    print (num)'''


