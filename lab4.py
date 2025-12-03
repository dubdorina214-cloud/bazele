#7
pozitive = 0
suma_pozitive= 0
numar_negative = 0
suma_negative= 0
print("introduceti 10 numere intregi:")
for _ in range(10):
    x = int(input(...))
    if x > 0:
        pozitive += 1
        suma_pozitive += x
    elif x < 0:
        numar_negative +=1 
        suma_negative +=x
print("numere pozitive:", pozitive)
print("suma numerelor pozitive:",suma_pozitive)
if  numar_negative>0 :
    print("media aritmetica a numerelor negative")
    print("suma numerelor pozitive:",pozitive)
    if numar_negative > 0:
        print("media aritmetica a numerelor negative:",suma_negative/numar_negative)
    else:
        print("nu exista numere negative")


''' #12
suma_dorita = int(input("introduceti suma dorita: ")) 
for i in range(10,100):
        s = (i // 10) + (i % 10)
        if s == suma_dorita:
            print (i)'''




'''#15
n = int(input("introduceti n:"))
if(n-1) % 2 ==0:
   x = (n- 1)//2
   print(f"{n} = {x} + {x + 1}") 
else:
   print("nu e posibil")'''





