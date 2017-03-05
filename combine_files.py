import glob
files = glob.glob( '*.txt' )

with open( 'result.txt', 'w' ) as result:
    for file_ in files:
        for line in open( file_, 'r' ):
            result.write( line )