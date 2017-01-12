import primes

#for i in xrange(24):
    #print "Fermat: {0}, result: {1}".format(i, primes.fermatTest(i))
    #print "MillerRabin: {0}, result: {1}".format(i, primes.millerRabin(i))
    #print "isPrime: {0}, result: {1}".format(i, primes.isPrime(i))
    #print "\n"

assert primes.isPrime(1) == True
assert primes.isPrime(2) == True
assert primes.isPrime(3) == True
assert primes.isPrime(4) == False
assert primes.fermatTest(5) == True
assert primes.millerRabin(5) == False
assert primes.isPrime(5) == True
assert primes.isPrime(6) == False
assert primes.isPrime(7) == True
assert primes.isPrime(8) == False
assert primes.isPrime(11) == True
assert primes.isPrime(13) == True
assert primes.isPrime(17) == True
assert primes.isPrime(19) == True
assert primes.isPrime(23) == True

