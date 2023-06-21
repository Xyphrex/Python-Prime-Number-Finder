import math
#from time import perf_counter #all timer code was used to graph times
import time
num = 3
prevnum = [2, 3] #hold previous primes
rootnum = math.ceil(math.sqrt(num)) #only tests divisors up to
#half the number being tested as any number cant be split evenly by a number
#larger than half of it E.G. 100 only has whole number devisors at 50 or below
counter = 0
count = 0
divisor = 2
#timer_start = perf_counter()
input()
while True:
    while divisor <= rootnum: #stores halfnum as variable so less calculation take place per test cycle
        if num % divisor == 0: #if tests if number isnt prime given a divisor
            num += 2
            divisor = 2
            counter = 0
        else: #passed if test and iterate counter to try new devisor
            counter += 1
            divisor = prevnum[counter]
    print(num) #once divisor gets halfway to num without any whole number divisions it is proven to be prime
    rootnum = math.ceil(math.sqrt(num))
#    timer_stop = perf_counter()
#    time = timer_stop - timer_start
#    Times = open("Times.txt", "a")
#    Times.write((str(time) + "\n"))
    count += 1
    if count > 1000000:
#        timer_stop = perf_counter()
#        print("completed with a time of:", timer_stop - timer_start)
        print("finished")
        input()
    prevnum.append(num) #appends found prime to array to be used later
    counter =  0
    divisor = 2
    num = num + 2
