from interpreter import draw
from chessPictures import *

rep = square.join(square.negative())

tablero = rep.horizontalRepeat(4)

draw(tablero)