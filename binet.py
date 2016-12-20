import numpy

phi = numpy.float128(( 1 + 5 ** 0.5) / 2)
reciprocalphi = numpy.float128( 1 - phi )


def binetFormula( number ):
    number = numpy.float128(number)
    result = (( phi ** number ) - (reciprocalphi ** number))/ numpy.float128(5 ** 0.5)
    return int( result )

