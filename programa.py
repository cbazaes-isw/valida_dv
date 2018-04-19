# pylint: disable=C0103
"""
high level support for doing this and that.
"""
import sys
import re
from util import getFactores

def main():
    """
    Holo main
    """

    param1 = sys.argv[1]
    # param1 = "b99mjsdf5q3f3o3i1i0..,-4"
    # param1 = "1-9"

    # [^\dk] Regex match todos los caracteres que no pertenecen al RUT.
    # Se limpia el parámetro de entrada asumiendo que el último
    # caracter (ya sea número o K) corresponde al dígito verificador.
    aux1 = re.sub(r"[^\dk]", "", param1, flags=re.IGNORECASE)

    # Se quita el último dígito para mantener solo el cuerpo del RUT
    # y se reversa el string
    cuerpo_rut = aux1[:len(aux1) - 1][::-1]

    # Con la cantidad de dígitos del cuerpo del rut preparo la lista de
    # factores para realizar la multiplicación de cada uno de los dígitos.
    factores = getFactores(len(cuerpo_rut))

    # Acumulo la multiplicación de los factores por cada dígito del cuerpo
    # del RUT.
    multiplicaciones = [factores[i] * int(cuerpo_rut[i]) for i in range(len(cuerpo_rut))]
    suma = sum(multiplicaciones)

    # Determino el dígito verificador con la diferencia entre 11 y el
    # resto del acumulado y 11. Si el resultado es menor a 10, el resultado
    # es el DV, de lo contrario es K.
    resultado = (11 - suma % 11)
    dv = "K"
    if resultado < 10:
        dv = resultado

    return dv

res = main()
print(res)
