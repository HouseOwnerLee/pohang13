i = 1

odd = 0
even = 0

while i < 101:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i+=1

print("홀수의 합:",odd)
print("짝수의 합:",even)