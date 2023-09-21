a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = (b**2) - (4 * a * c)
raizd = delta ** 0.5
if delta < 0:
    print('sem raiz real')
elif delta == 0:
    print('equação com 1 raiz real')
    x1 = (-b + raizd)/(2*a)
    x2 = (-b - raizd)/(2*a)
    print('x1 = {:.2f}, x2 = {:.2f}'. format(x1,x2))
elif delta > 0:
    print('equação com 2 raizes reais')
    x1 = (-b + raizd)/(2*a)
    x2 = (-b - raizd)/(2*a)
    print('x1 = {:.2f}, x2 = {:.2f}'. format(x1,x2))


