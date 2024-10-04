def s_prime(wrapper):
    return wrapper
@ s_prime
def sum_three(*args):
    b = sum(args)
    f = 'Простое число'
    for i in range(2,b-1):
        if b%i == 0:
            f='Составное число'
    print(f)
    return b

sum_three = s_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)