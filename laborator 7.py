
#7
'''
k_str = input().strip()
if not k_str.isdigit():
    print("Ошибка: введите натуральное число.")
else:
    k = int(k_str)
if k < 100 or k > 9999999:
        print("Ошибка: число должно быть от 3 до 7 цифр.")
else:
        k1 = k // 10
        temp = k1
        p = 1
while temp >= 10:
            temp = temp // 10
            p = p * 10
result = k1 % p
print(result)'''



#8
'''
while True:
    print("Введите сторону a:")
    a = int(input())

    print("Введите сторону b:")
    b = int(input())

    print("Введите сторону c:")
    c = int(input())
    if a == 0 or b == 0 or c == 0:
        print("Завершено.")
        break
    if a + b > c and a + c > b and b + c > a:
        print("True")
    else:
        print("False")'''




 #10
n = input("Введите 6-значное число: ")
if len(n) != 6 or not n.isdigit():
    print("Ошибка: нужно ввести ровно 6 цифр.")
else: 
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    d = int(n[3])
    e = int(n[4])
    f = int(n[5])

    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and \
       d % 2 == 1 and e % 2 == 1 and f % 2 == 1:
        print("DA")
    else:
        print("NU")
        



    
