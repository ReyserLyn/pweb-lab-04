from interpreter import draw
from chessPictures import *

caballoBlanco = knight
caballoNegro = knight.negative()

tablero = caballoBlanco.join(caballoNegro).up(caballoNegro.join(caballoBlanco))

draw(tablero)