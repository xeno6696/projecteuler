import primes

for i in xrange(24):
    print "testingFermat: {0}, result: {1}".format(i, primes.fermatTest(i))
    print "testingMillerRabin: {0}, result: {1}".format(i, primes.millerRabin(i))
