keys = input().split()
vales = map(int,input().split())

dct = dict(zip(keys,vales))

target = []
del dct['delta']
for key,val in dct.items():
    if val == 30:
        target.append(key)

for i in target:
    del dct[i]

print(dct)