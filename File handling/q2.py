name = input("Enter student name: ")
marks = float(input("Enter marks: "))

with open("question.txt", "w") as file:
        file.write(f"{name},{marks}\n")
        print("Data saved successfully!\n")

with open("question.txt", "r") as file:
        content = file.read()

print(content)
