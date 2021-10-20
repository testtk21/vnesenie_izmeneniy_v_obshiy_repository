import math

print('A * x^2 + B * x + C = 0\nInsert coefficients for the equation:')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))

D = b ** 2 - 4 * a * c


if D > 0:
    x1 = (-b + math.sqrt(D) / (2 * a))
    x2 = (-b - math.sqrt(D) / (2 * a))
    print('X1 = ', x1, '\nX2 = ', x2)
elif D == 0:
    x = -b / (2 * a)
    print('X = ', x)
else:
    print('There is no solutions')
    
print('Discriminant D = ', D)
