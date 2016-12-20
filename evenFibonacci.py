import binet, integers, math, numpy

answer = numpy.double(0)

MAX = numpy.double(4000000)

for i in range( 0, int( math.sqrt( MAX ))):
    term = binet.binetFormula( i ) 
    if integers.isEven( term ) :
#        print "term: %f" % term
#        print "MAX: %f" % MAX
#        print "term < MAX:" +  str(term < MAX)
        if term < MAX:
            answer += term
#            print term
        else:
            break

print '%d' % answer        
