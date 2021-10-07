import math

def isPrime(number):
    stop_looking = math.floor(number / 2)

    for divisor_check in range(2, stop_looking):
        if number % divisor_check == 0:
            return False
    return True

def countPrimes(number_range):
    print("we want to know how many numbers less than", number_range, "are prime")

    number_of_primes = 0

    for number in range(2, number_range):
        if isPrime(number):
            number_of_primes += 1

    print(number_of_primes)

if __name__ == "__main__":
    countPrimes(10)
    countPrimes(100)
    countPrimes(1000)
    countPrimes(10000)
    countPrimes(100000)
    countPrimes(1000000)
    countPrimes(10000000)
    countPrimes(100000000)
