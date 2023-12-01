import fileinput, re

d = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }

print( sum( d[ re.search( "(" + "|".join( d.keys() ) + ")", l ).group( 1 ) ] * 10 +
            d[ re.search( "(?s:.*)(" + "|".join( d.keys() ) + ")", l ).group( 1 ) ]
            for l in fileinput.input("input.txt") ) )