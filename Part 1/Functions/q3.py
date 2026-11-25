
def average(marks):
    if len(marks) == 0:
        return 0                 
    return sum(marks) / len(marks)

print(average([85, 90, 78]))     
print(average([]))              