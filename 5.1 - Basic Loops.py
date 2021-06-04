'''
Pirple Homework #5.1:
    Loops
        Basic Loops

Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

Extra Credit:
Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime".
You should print this whenever you encounter a number that is prime (divisible only by itself and one).
As you implement this, don't worry about the efficiency of the algorithm you use to check for primes.
It's okay for it to be slow.
'''

def checkPrime(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return False
    else:
        return True

def FizzBuzz():
    for num in range(1,101):
        if checkPrime(num):
            print(num,"Prime")
        elif num % 5 == 0 and num % 3 == 0:
            print(num, "FizzBuzz")
        elif num % 3 == 0:
            print(num, "Fizz")
        elif num % 5 == 0:
            print(num, "Buzz")
        else:
            print(num)

FizzBuzz()