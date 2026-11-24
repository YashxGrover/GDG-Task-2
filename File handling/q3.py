try:
 marks = float(input("Enter student marks: "))
 print(f"Marks recorded: {marks}")
except ValueError:
    print("Invalid input! Please enter numbers only ")
