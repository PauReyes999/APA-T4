"""
Nombre del alumno: Pau Reyes Boix
Descripción: Este script implementa un generador de números oaleatorios
basado en el método del Generador Lineal Congruente (LGC). Se incluyen dos formas
de generación: una clase llamada Aleat que actúa como iterador y una función
generadora aleat() con capacidad de reinicio dinámico mediante send().

Ambas soluciones generan secuencias de enteros dentro del rango [0, m).

Pruebas:
- Incluye tests integrados usando doctest para verificar el funcionamiento de ambas implementaciones.
"""

class Aleat:
    """
    Clase que implementa un generador pseudoaleatorio con el algoritmo LGC.

    Fórmula usada:
        xₙ₊₁ = (a * xₙ + c) % m

    Atributos:
    - m: Módulo (valor máximo excluyente)
    - a: Multiplicador
    - c: Incremento
    - x: Valor actual de la secuencia

    Métodos:
    - __next__(): Devuelve el siguiente número pseudoaleatorio
    - __call__(semilla): Reinicia la secuencia con una nueva semilla

    >>> gen = Aleat(m=32, a=9, c=13, semilla=11)
    >>> for _ in range(4):
    ...     print(next(gen))
    16
    29
    18
    15

    >>> gen(29)
    >>> for _ in range(4):
    ...     print(next(gen))
    18
    15
    20
    1
    """

    def __init__(self, m=2**48, a=25214903917, c=11, semilla=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = semilla

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nueva_semilla):
        self.x = nueva_semilla


def aleat(m=2**48, a=25214903917, c=11, semilla=1212121):
    """
    Generador LGC. Produce infinitos números pseudoaleatorios.

    Parámetros:
    - m: Módulo (máximo valor excluyente)
    - a: Multiplicador
    - c: Incremento
    - semilla: Valor inicial

    Devuelve:
    - Un generador infinito que permite reinicio mediante .send()

    >>> g = aleat(m=64, a=5, c=46, semilla=36)
    >>> for _ in range(4):
    ...     print(next(g))
    34
    24
    38
    44

    >>> g.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(g))
    44
    10
    32
    14
    """

    x = semilla
    while True:
        x = (a * x + c) % m
        nueva = yield x
        if nueva is not None:
            x = nueva


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
