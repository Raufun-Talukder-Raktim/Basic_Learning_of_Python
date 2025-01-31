from Tuples import output

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "\U0001F600"
}
output = ""
for word in words:
    output += emojis.get(word, word)+ " "
print(output)
print("\U0001F600")