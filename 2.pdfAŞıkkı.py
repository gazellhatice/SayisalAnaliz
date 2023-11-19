def f(x):
    return x*x*x-2*x*x-5

a = int(input("İlk deger: "))
b = int(input("İkinci deger: "))
i = int(input("iterasyon sayisi: "))
sayac = 0

while(sayac<=i):
    c = (a+b)/2
    if(f(c)*f(b) < 0):
        a = c
    if(f(a)*f(c) < 0):
        b = c
        sayac = sayac+1
        print("root is: ",c)
