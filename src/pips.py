from enum import Enum, unique


@unique
class Pips(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - {pip.value}


if __name__ == "__main__":
    print(list(Pips))
    """Se muestra una lista de los pares nombre valor por consola. Ya que se listan los valores del tipo enumerado"""
    print(Pips(1))
    print(Pips["ONE"])
    print(Pips.ONE)
    """En este caso se muestra las claves del valor uno con distintas formas de buscarla """
    print(Pips.ONE.name)
    """Muestra el nombre del miembro ONE del enum."""
    print(Pips.ONE.value)
    """Muestra el valor de la clave dada"""
    for number in Pips.__members__.values():
        print(number._value_)
    """Utiliza la el mismo metodo que arriba solo que ahora lo mete en un "for" para recorrer todos los miembros del enum."""

    print(Pips.values())
    """Muestra todos los valores del enum """
    print(Pips.reversedValues())
    """Llama al metodo reversedValues de Pips, donde este devuelve los valores en una lista de forma inversa"""
    print(Pips.minus(Pips.FIVE))
    """Muestra todos los valores del enum menos el valor de la clave dada """
