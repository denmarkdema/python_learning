#切片
L = ['a', 'b',  'c', 'd', 'e', 'f']
r = []
n = 3
for nums in range(n):
    r.append(L[nums])
print(r)

#map/reduce
def f(x):
    return x * x

r = map(f, list(range(8)))
print(list(r))

