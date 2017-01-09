import primes

for i in xrange(24):
    print "Fermat: {0}, result: {1}".format(i, primes.fermatTest(i))
    print "MillerRabin: {0}, result: {1}".format(i, primes.millerRabin(i))
    print "isPrime: {0}, result: {1}".format(i, primes.isPrime(i))
    print "\n"

