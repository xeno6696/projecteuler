import math, binet

def isPrime( p ):
    print fermatTest(p)

def fermatTest( p ):
    isPrime = False
    print "Testing %d " % p
    positives = 0
    negatives = 0
    for i in range( 2, p - 1):
        raised = i **(int(p) - 1)
        #print "raised: %d" % raised
        isCongruent = raised == 1 % p
        print isCongruent
        if(isCongruent):
            positives += 1
        else:
            negatives += 1
        

    if(positives > negatives):
        isPrime = True
    return isPrime
