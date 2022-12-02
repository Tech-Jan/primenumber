
def prime_checker(number):
    is_prime = True
    i = 2
    while i in range(2, int(number - 1)) and is_prime == True:
        modcheck = number % i
        # print(modcheck)
        if modcheck == 0:
            is_prime = False
        i += 1
    print(is_prime)


n = int(input("Check this number: "))
prime_checker(number=n)

