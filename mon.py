def f1( param ):
  return ( param+1, str( param ) + "+1" )
  
def f2( param ):
  return ( param+2, str( param ) + "+2" )
  
def f3( param ):
  return ( param+3, str( param ) + "+3" )

def unit( param ):
  return ( param, "Operations: " )
  
def bind( ntuple, funxtion ):
  result = funxtion( ntuple[ 0 ] )
  return ( result[ 0 ], ntuple[ 1 ] + result[ 1 ] + ";" )
  
print( bind( bind( bind(unit( x ), f1 ), f2 ), f3 ) )
