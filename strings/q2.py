
marks = []
for i in range(5):
    m = float(input(f"Enter mark {i+1}: "))
         marks.append(m)

total = 0
highest = marks[0]               
lowest = marks[0]

for m in marks:
    total += m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

average = total / len(marks)

print(f"Total:   {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")