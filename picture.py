from colors import *


class Picture:
    def __init__(self, img):
        self.img = img;

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        return Picture(self.img[::-1])

    def horizontalMirror(self):
        """Devuelve el espejo horizontal de la imagen"""
        return Picture([value[::-1] for value in self.img])

    def negative(self):
        """ Devuelve un negativo de la imagen """
        return Picture([[self._invColor(color) for color in row] for row in self.img])

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento
            al lado derecho de la figura actual """
        new_img = [list(row1) + list(row2) for row1, row2 in zip(self.img, p.img)]
        return Picture(new_img)

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p encima de la
            figura actual """
        new_img = []
        for row1, row2 in zip(self.img, p.img):
            new_row = [pixel2 if pixel1 == ' ' else pixel1 for pixel1, pixel2 in zip(row1, row2)]
            new_img.append(new_row)
        return Picture(new_img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p debajo de la
            figura actual """
        return Picture(self.img + p.img)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual a la derecha
            la cantidad de veces que indique el valor de n """
        return Picture([row * n for row in self.img])

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
            la cantidad de veces que indique el valor de n """
        return Picture(self.img * n)

    # Extra: Sólo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
        return Picture(None)
