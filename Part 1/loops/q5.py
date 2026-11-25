for j in range(2, 101):             
    is_prime = True                 
    for i in range(2, j):           
        if j % i == 0:
            is_prime = False
            break
    if is_prime:
        print(j)