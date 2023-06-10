from interpreter import draw
from chessPictures import *

rep = square.negative().join(square)
tablero = rep.horizontalRepeat(4)

draw(tablero)