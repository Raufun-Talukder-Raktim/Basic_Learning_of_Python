number3 = [1,2,4,4,5,6,72,32,5,6,6,4,4,4,6]
number3.sort()
number_copy = number3.copy()
print(number3)
print(number_copy)
x =0
value =0
print('start')
while x < len(number3):
    count =0
    y = x+1
    iteration = 0
    if x < len(number3):
        while y < len(number3):
            iteration = y
            print(f'x ={x} , y ={y}')

            if number3[x] == number3[y]:
                print('ok')
                #value = number3[y]
                #print(value)
                number_copy.pop(iteration-value)
                value+=1
                count += 1
                #iteration-=1
                #number3.remove(value)
                print(number_copy)
                print(f'increase {x}')
            y+=1
    x +=count
    x+=1
    #print(x)



