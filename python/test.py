a = input().split()
count = 0

for word in a:
    if word.strip(',.') == 'the':
        count += 1

print(count)