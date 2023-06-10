from interpreter import draw
from chessPictures import *

columna1 = square.join(square.negative()).horizontalRepeat(4)
columna2 = square.negative().join(square).horizontalRepeat(4)

tablero = columna1.under(columna2).verticalRepeat(2)

draw(tablero)