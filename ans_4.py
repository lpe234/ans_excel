# -*- coding: utf-8 -*-


a = [1, 1, 1, 1, 1, 2, 3, 3, 4]
b = []

index = 0


for x in a:
    if b:
        if b[-1] == x:
            continue
    b.append(x)
print b