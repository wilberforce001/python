# For loops iterate over a given sequence
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

#The range function returns a new list with numbers of that specified range.
#xrange returns an iterator, which is more efficient.

for x in range(5):
    #Prints out the numbers 0,1,2,3,4
    print(x)

for x in range(3, 6):
    #prints out 3,4,5
    print(x)
for x in range(3, 8, 2):
    #prints out 3,5,7
    print(x)