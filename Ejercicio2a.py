from interpreter import draw
from chessPictures import *

caballoBlanco = knight
caballoNegro = knight.negative()

tablero = caballoBlanco.join(caballoNegro).under(caballoNegro.join(caballoBlanco))

draw(tablero)