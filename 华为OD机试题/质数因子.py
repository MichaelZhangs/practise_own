def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def digui(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime_number(i):
            n = n // i
            print(i, end=" ")
            digui(n)
            break

n =int(input())
digui(n)
