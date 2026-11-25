

try:
    with open("ques.txt", "r") as file:
        content = file.read().strip()
        if not content:
            print("The file is empty. No data to display.")
        else:
            print("Saved Data:")
            print(content)
except FileNotFoundError:
    print(f"Error: The file ques.txt does not exist yet.")
