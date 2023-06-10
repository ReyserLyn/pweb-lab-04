from interpreter import draw
from chessPictures import *

caballoBlanco = knight
caballoNegro = knight.negative()

columna1 = caballoBlanco.join(caballoNegro)
columna2 = caballoNegro.horizontalMirror().join(caballoBlanco.horizontalMirror())

tablero = columna1.under(columna2)
draw(tablero)