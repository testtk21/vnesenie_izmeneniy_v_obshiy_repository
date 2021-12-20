import math

print('A * x^2 + B * x + C = 0\nВведите коэффициенты квадратного уравнения:')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))
D = B * B - 4 * A * C
print("Дискриминант D = " , D)
if D >0:
    X1 = (- B + math.sqrt(D))/2 * A
    X2 = (- B - math.sqrt(D))/2 * A
    print("X1 = " , X1)
    print("X2 = " , X2)
elif D == 0:      
    X = - B / 2 * A
    print("X = " , X)
else:
    print("Вещественных корней нет")
