# Даны три множества a, b и с.
# Необходимо выполнить все изученные виды бинарных операций над всеми комбинациями множеств.

a = set('12345')
b = set('159')
c = set()

ab = a.union(b)                     #объединение
ab2 = a.intersection(b)             #пересечение
ab3 = a.difference(b)               #разность
ba = b.difference(a)                #разность
ab4 = a.symmetric_difference(b)     #симметрическая разность
ac = a.union(c)
ac2 = a.intersection(c)
ac3 = a.difference(c)
ca = c.difference(a)
ac4 = a.symmetric_difference(c)
bc = b.union(c)
bc2 = b.intersection(c)
bc3 = b.difference(c)
cb = c.difference(b)
bc4 = b.symmetric_difference(c)