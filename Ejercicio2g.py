from interpreter import draw
from chessPictures import *

columna1 = square.join(square.negative()).horizontalRepeat(4)
columna2 = square.negative().join(square).horizontalRepeat(4)

tablero = columna1.under(columna2).verticalRepeat(4)

peones = pawn.horizontalRepeat(8)
negras = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock).under(peones).negative()
espacios = columna1.under(columna2).verticalRepeat(2)
blancas = peones.under(rock.join(knight).join(bishop).join(king).join(queen).join(bishop).join(knight).join(rock))

piezas = negras.under(espacios).under(blancas)



draw(piezas.up(tablero))