#Emily Nixon

def perfect_number(x):
    divisors_sum=0
    for y in range(1, x):
        if x%y == 0:
            divisors_sum += y
    if divisors_sum == x:
        return True
    else:
        return False

print(perfect_number(6))
print(perfect_number(29))
