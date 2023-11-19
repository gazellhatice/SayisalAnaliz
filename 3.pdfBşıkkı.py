import math

x = 2
error = 10**-6
iter = 4
def func(x):
    f_x = (4*math.e**-0.5*x) - x
    return f_x

def dfunc(x):
    df_x = (-2*math.e**-0.5) -1
    return df_x

for i in range(1,iter):
    f_x = func(x)
    df_x = dfunc(x)
    print ( str(i) + 'x: ' + str(x) + ' f(x): ' +str(f_x) )
    if abs(f_x) < error:
        break
    x = x-f_x/df_x
