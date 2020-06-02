# 2. n번째 소수

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

def prime_number_list(length):
    result = []
    n = 0
    while True:
        n += 1
        if(is_prime(n) == True):
            result.append(n)
        elif(len(result) == length):
            break
    return result

length = int(input('Length? '))
print(prime_number_list(length))