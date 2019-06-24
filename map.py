>>> import math
>>> lista1 = [1, 4, 9, 16, 25]
>>> lista2 = map(math.sqrt, lista1)
>>> print lista2
[1.0, 2.0, 3.0, 4.0, 5.0]

>>> lista2 = [math.sqrt(x) for x in lista1]
>>> print lista2
[1.0, 2.0, 3.0, 4.0, 5.0]
