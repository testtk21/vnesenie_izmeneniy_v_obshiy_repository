import math

print('A * x^2 + B * x + C = 0\nВведите коэффициенты квадратного уравнения:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))
D = B**2 - 4 * a * c
print ('Дискриминант D = ', D)
if D > 0:
    X1 = (-B + math.sqrt(D)) / 2 * a
    X2 = (-B - math.sqrt(D)) / 2 * a
    print ('X1=', X1)
    print ('X2=', X2)

elif D == 0:
    X = -B / 2 * a
    print ('X=', X)
    
else:
    print ('Вещественных корней нет')

