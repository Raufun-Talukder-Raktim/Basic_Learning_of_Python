from string import digits

from for_loop import output

coordinates = (1,2,3)
x,y,z = coordinates
print(x)

customer = {
    "name": "Raktim",
    "Age": 23,
    "is_valid": True
}

print(customer["name"])
print(customer.get("Age"))
print(customer.get("phone", "017033"))

phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)