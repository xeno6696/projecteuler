import math, binet, random

def isPrime( p ):
    return fermatTest(p) and not millerRabin(p)

#Heuristic test that returns if a number is "probably prime."
def fermatTest( p ):
    isPrime = False
    #print "Testing %d " % p
    positives = 0
    negatives = 0
    if p == 1:
        return True
    elif p == 2:
        return True
    elif p % 2 == 0:
        return False
    
    for i in xrange(p):
        answer = random.randint(1, p - 1)
        raised = pow(answer, p-1) % p
        #print "pow({0}, {1}-1) % {2} == {3}".format(answer, p, p, raised)
        
        if raised == 1:
            positives +=1
        else:
            negatives +=1

        if positives > negatives:
            isPrime = True
        
    return isPrime

def millerRabin( p ):
    isComposite = False

    if p == 2:
        return False
    elif p % 2 == 0: 
        return True
    elif p == 0 or p == 1 or p == 3:
        return False

    #Formula requires the expression 2s*d where it represents factoring
    #all powers of 2 from n - 1
    r = p - 1
    s = 0
    #Also could use divmod... returns a quotient and remainder...
    while r % 2 == 0:
        s += 1
        print "Factoring 2 from {0}".format(r)
        r /= 2

    print "asserting 2**{0} * {1} = {2} and {3}-1={4}".format(s, r, 2**s *r, p, p-1)
    assert(2**s * r == p-1)
    isComposite = try_composite(p, r)
    
    return isComposite

def try_composite(p, r):
    
    for i in xrange(p):
        #print "p is {0}".format(p)
        a = random.randint(2, p)
        
        y = pow(a, r, p)
        print "computing:  {0}**{1} % {2} == {3}".format(a, r, p, y)
        if y == 1:            
            return False
        if y != p-1:
            return False
    
    return True
    
