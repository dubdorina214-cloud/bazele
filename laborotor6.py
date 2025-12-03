'''#3
a = float(input("введите сторону a:"))
b= float(input("введите сторону b:"))
area = a*b
perimetr=2 * (a + b )
print ("площадь =", area)
print("периметр =",perimetr)'''


'''#5
n = int(input("введите число:"))
s = 0
for i in range (1,n ):
    if n % i == 0:
        s += i
        if s == n:
            print ("число совершенное")
        else:
            print("число не совершенное")'''

#7
n = int(input("введите число:"))
rev= 0
while n > 0:
 d=n % 10
 rev = rev * 10 + d
 n=n//10
print(rev)

