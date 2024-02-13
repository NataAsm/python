import random
a = []
for i in range(5):
    A = random.randint(1, 99)
    a.append(A)
    print(a[i])

r = max(a)
print('-------------------')
print(r)

d = a.pop(4)
print('-------------------')
print(d)

