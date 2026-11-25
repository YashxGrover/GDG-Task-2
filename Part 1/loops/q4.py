word = input("Word: ")
word = word.lower

count = 0
for i in range(len(word)):       
    if word[i] in "aeiou":
        count += 1

print(f"Vowels: {count}")