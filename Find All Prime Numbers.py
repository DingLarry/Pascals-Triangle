"""
This method uses the Sieve of Eratosthenes, first we need to create a list starting from 2, and then we get the first number 2, use it to be divided by the rest of that list, and keep those numbers whose reminder is not 0, and those numbers consist the second list. Then we can get the first number of second list, and use it to be divided by the rest of numbers and also keep the number of whose reminder is not 0. we keep doing this and finally we can get all the prime numbers among all natural numbers.
"""
#Below are the code
#First, we need to create a list containing all numbers from 3.
def AllNumber():
    n = 1
    while True:
        n = n +2
        yield n

#Second, we need to create a filter to filter out those numbers whose reminders are 0
def Filter(n):
    return lambda x: x%n >0

#Third, we need to create a generator to store the logic.
def FindAllPrimes():
    yield 2
    it = AllNumber() #Initialize the list
    while True:
       n = next(it) #Return the first number of the list
       yield n
       it = filter(Filter(n),it) #Reform a new list
"""
One thing, I have noticed that for the function in filter argument, it doesn't need to strictly have two parameters but it can define a parameter youself and then get another paramter from the list.
"""
