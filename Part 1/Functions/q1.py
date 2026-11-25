
def largest(a, b, c):
    largest = a                
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest              

print(largest(3, 9, 5))    