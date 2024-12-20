# Functions with outputs
def sumar(a, b):
    result = a + b
    return result

print(sumar(2,3))
# title() returns the first capitalized
def format_name(last_name, first_name):
    return last_name.title() + " " + first_name.title()

print(format_name("angel", "serrato"))
# Leap year
def is_leap_year(year):
    """
    Determina si un año dado es bisiesto o no.

    Un año es bisiesto si:
    - Es divisible por 4, pero no es divisible por 100, o
    - Es divisible por 400.

    Args:
        year (int): El año que se desea verificar.

    Returns:
        bool: Retorna `True` si el año es bisiesto, de lo contrario retorna `False`.

    Ejemplos:
        >>> is_leap_year(2000)
        True

        >>> is_leap_year(2024)
        True

        >>> is_leap_year(2023)
        False
    """
    if year % 4 == 0:  # Si es divisible por 4, puede ser bisiesto
        if year % 100 == 0:  # Si es divisible por 100, chequeamos si es divisible por 400
            if year % 400 == 0:  # Si es divisible por 400, es bisiesto
                return True
            else:
                return False
        else:
            return True  # Si es divisible por 4, pero no por 100, es bisiesto
    else:
        return False  # Si no es divisible por 4, no es bisiesto
# Ejemplo de prueba:
print(is_leap_year(2001))  # Esto debería retornar False
# Docstrings