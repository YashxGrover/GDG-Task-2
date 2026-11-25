
names = ["Yash", "parth", "lakshay", "vansh"]
target = input("Search: ")

if target in names:
    print(f"{target} found at position {names.index(target)}")
else:
    print(f"{target} not found")