# TODO: Implementa el código del ejercicio aquí

import re

class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(char.isupper() for char in clave)

    def _contiene_minuscula(self, clave):
        return any(char.islower() for char in clave)

    def _contiene_numero(self, clave):
        return any(char.isdigit() for char in clave)

    def es_valida(self, clave):
        raise NotImplementedError


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def _contiene_caracter_especial(self, clave):
        return any(char in '@_#$%' for char in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise ValueError("La clave no tiene la longitud esperada")
        if not self._contiene_mayuscula(clave):
            raise ValueError("La clave no contiene una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise ValueError("La clave no contiene una letra minúscula")
        if not self._contiene_numero(clave):
            raise ValueError("La clave no contiene un número")
        if not self._contiene_caracter_especial(clave):
            raise ValueError("La clave no contiene un caracter especial")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def _contiene_calisto(self, clave):
        calisto = re.findall('calisto', clave, re.IGNORECASE)
        for word in calisto:
            if sum(1 for c in word if c.isupper()) >= 2:
                return True
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise ValueError("La clave no tiene la longitud esperada")
        if not self._contiene_numero(clave):
            raise ValueError("La clave no contiene un número")
        if not self._contiene_calisto(clave):
            raise ValueError("La clave no contiene 'calisto' con al menos dos letras mayúsculas")
        return True


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
