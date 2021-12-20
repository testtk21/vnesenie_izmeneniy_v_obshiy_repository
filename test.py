import math

print('A * x^2 + B * x + C = 0\nВведите коэффициенты квадратного уравнения:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

D=b*b - 4*a*c
if D > 0:
    x1=(-b+math.sqrt(D))/2*a
    print('x1 =',x1)
    x2=(-b-math.sqrt(D))/2*a
    print('x2 =',x2)
elif D==0:
    x=-b/2*a
    print('x =',x)
else:
    print('Вещественных корней нет')
