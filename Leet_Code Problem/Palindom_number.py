from contextlib import nullcontext
from itertools import count

number = 12131212
output = []
output_check = []
str_number = str(number)
length = len(str(number))
for i in str_number:
    output.append(i)
output_check = output.copy()
output_check.reverse()
count = True
print(length)
i =0
while i < length:
    if output[i] != output_check[i]:
#        print("False")
        count = False

    i+=1
print(count)
#if count is True:
#    print("True")
#elif count is False:
#    print("False")