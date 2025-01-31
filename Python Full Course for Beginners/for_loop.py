from contextlib import nullcontext

total = 0
for item in ['10','20','30']:
    single_value = int(item)
    total = single_value+total
print(f'total {total}')

for x in range(3):
    for y in range(3):
        print(f"{x}, {y}")

number = [5,2,5,2,2]
for x in number:
    output= ''
    for y in range(0,x):
        output += "x"
    print(output)



