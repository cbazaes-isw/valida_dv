# pylint: disable=C0103
"""
high level support for doing this and that.
"""
def getFactores(largo):
    """
    Determino la lista con los factores que serán utilizados para el cálculo
    del DV.

    La lista de factores en función del largo del cuerpo del RUT tiene
    los siguientes valores:

    LARGO   :   1   2   3   4   5   6
    
    FACTOR  :   2   3   4   5   6   7

    La lista de factores se repite si el largo del cuerpo del RUT es mayor
    a 6, de la siguiente manera: Asumiendo que tenemos un RUT de largo 9 la
    lista de factores sería la siguiente:

    factores = [2, 3, 4, 5, 6, 7, 2, 3, 4]
    """
    factores = []

    # Determino la cantidad de veces que tengo que agregar el rango(2-7) de
    # forma completa en la lista factores.
    iteraciones = 1
    if largo % 6 != 0:
        iteraciones += int(largo / 6)
    
    # Agrego el rango(2-7) tantas veces como fueron determinadas en el paso
    # anterior. Aquí es importante recordar que el método range(2, 8) permite
    # crear la siguiente lista [2, 3, 4, 5, 6, 7] ya que el 8 no se incluye.
    for i in range(iteraciones):
        factores.extend(range(2, 8))

    # De la lista de factores resultantes solo recupero la cantidad de
    # elementos de acuerdo al largo del cuerpo del RUT.
    return factores[:largo]
