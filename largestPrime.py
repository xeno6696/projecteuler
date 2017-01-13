import primes, math

factor = 600851475143

root = math.sqrt(factor)

for i in reversed( range( int( math.ceil(root)))):
    print "Testing number [{0}]".format(i)
    if i % 2 != 0 and primes.isPrime( i , 5):
        print i
        break
