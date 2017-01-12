import primes

knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541 ]

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

for i in knownPrimes:
    assert primes.isPrime(i) == True
