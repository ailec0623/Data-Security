a = []
b = []
for i in range(0,10):
    a.append(i)
    b.append(a[:])
for i in b:
    print(i)