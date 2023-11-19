def f(x):
    return x*3 + 4*x*2 - 10

a = 1
b = 2
epsilon = 1e-6
iteration = 0

while (b - a) / 2 > epsilon and iteration < 4:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c
    iteration += 1

root = (a + b) / 2

print("Bulunan kök:", root)
print("Yapılan iterasyon sayısı:",iteration)