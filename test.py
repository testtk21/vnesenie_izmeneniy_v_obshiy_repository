import math

print('A * x^2 + B * x + C = 0\nВведите коэффициенты квадратного уравнения:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

#Вставить свой код здесь
D=b**2-4*a*c
print('D= '+str(D))

if D>0:
    x1=(-b+math.sqrt(D))/2*a
    x2=(-b-math.sqrt(D))/2*a
    print('x1= '+str(x1))
    print('x2= '+str(x2))
elif D==0:
    x=-b/2*a
    print('x= '+str(x))
else:
    print("Вещественных корней нет")
