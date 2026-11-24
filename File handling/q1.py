
with open("notes.txt", "w") as file:     
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")

with open("notes.txt", "r") as file:     
    content = file.read()

print("Read back:")
print(content)