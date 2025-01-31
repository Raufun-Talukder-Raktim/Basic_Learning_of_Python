names = ['jon','bob','mos','sar','mary']
names[1]= 'Raktim'
print(names)

largest_number = 0
number = [1002,1,2,3,4,5,6,72,574,32,6,566]
for i in range(len(number)):
    if largest_number < number[i]:
        largest_number = number[i]
    elif largest_number >= number[i]:
        largest_number = largest_number
print(largest_number)

max = number[0]
for i in number:
    if i > max:
        max = i
print(max)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0])

for row in matrix:
    for item in row:
        print(item)

number = [5,2,1,7,4]
number.append(13)
number.insert(0,10)
number.pop(4)
print(number)
number.sort()
number.reverse()
number2 = number.copy()
print(number)

