import math, binet, random

def isPrime( p ):
    print fermatTest(p)

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
        return True
    elif p % 2 == 0 or p == 1
        return False

    #Formula requires the expression 2s*d where it represents factoring
    #all powers of 2 from n - 1
    d = p - 1
    while x % 2 == 0 
    
    for i in xrange(p):
        a = random.randint(2, p-2)
          
    return isComposite
