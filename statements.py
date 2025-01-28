from age_calculator import weight

is_hot = False
is_cold = True
if is_hot:
    print("It is a hot day")
    print("Drink water")
elif is_cold:
    print("it is a cold day")
    print("Wear warm clothes")
else:
    print("it is a lovely day")
    print("enjoy your day")

has_high_income = True
has_good_credit = True

if has_good_credit or has_high_income:
    print("good for loan")

name = input()
name_length = len(name)

if name_length < 3:
    print("Name must be at least 3 characters long")
elif name_length >50:
    print("name can not be more than 50 characters long")
else:
    print("name looks good!")

print("enter your weight ")
weight = float(input())
print("(L)bs or (k)g: ")
l_or_k = input()

if l_or_k == 'k' or l_or_k == 'K':
    weight_l = weight / 0.45
    print(f'your name is {name}, your weight in KG is {weight}, and in lbs is{weight_l}')
elif l_or_k == 'l' or l_or_k == 'L':
    weight_kg = weight * 0.45
    print(f'your name is {name}, your weight in lbs is {weight}, and in kg is{weight_kg}')
else:
    print("Inter a valid input")


