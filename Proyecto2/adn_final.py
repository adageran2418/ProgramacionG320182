def es_base (caracter):
    '''
    (str) - bool

    Programa para validar si el caracter es parte de la base

    Programa para validar si una base es de la cadena

    >>> es_base('A')
    True

    >>> es_base('P')
    False

    >>> es_base('F')
    False

    :param base: ingresa una letra para saber si corresponde a una base
    :return: booleano
    '''
    bases = ["T", "A", "C", "G"]

    base_1 = False

    for i in bases:
        if (caracter == i):
            base_1 = True
    return base_1

def validar (base1, base2):

    '''
    (str,str) - (bool)
    Programa para validar si una base es de la cadena

    >>> validar('A','C')
    True

    >>> validar('P','C')
    False

    >>> validar('C','G')
    True

    :param base: ingresa una letra para saber si corresponde a una base
    :param base2: ingresa segunda letra para saber si corresponde a la base
    :return: booleano
    '''
    bases = ["T", "A", "C", "G"]

    base_1 = False

    for i in bases:
        if (base1 == i):
            base_1 = True
        else:
            (base2 == i)

    return base_1

def obt_compl(bases):
    '''
    (str) - (str)
    Programa para obtener solo el complemento

    >>> obt_compl("A")
    'T'

    >>> obt_compl("T")
    'A'

    >>> obt_compl("C")
    'G'

    :param base: Base a la cual se le va a buscar el complemento
    :return: Complemento
    '''
    complementos = ""
    if (bases == "A"):
        complementos = "T"

    elif (bases == "G"):
        complementos = "C"

    elif (bases == "T"):
        complementos = "A"
    else:
        complementos = "G"

    return complementos

def complemento_base (base):
    """
    (str)-> (str)
    Programa para complementar la base dada

    >>> complemento_base('T')
    'AT'

    >>> complemento_base('G')
    'CG'

    >>> complemento_base('C')
    'GC'

    :param base: base a complementar
    :return: base complementada
    """
    comp_base = ''

    if (base == 'C'):
        comp_base = 'G' + base
    elif (base == 'T'):
        comp_base = 'A' + base
    elif (base == 'G'):
        comp_base = 'C' + base
    else:
        comp_base = 'T'
    return comp_base

def porcentaje (cadena1, cadena2):
    """
    (str),(str)-> (float)
    Programa para hallar el porcentaje de correspondiente a las cadenas

    >>> porcentaje("CG","GA")
    50

    >>> porcentaje("AT","GT")
    0

    >>> porcentaje ("AAAT","GCGA")
    25

    :param cadena1: primera cadena ingresada
    :param cadena2: segunda cadena ingresada
    :return: porcentaje de similitud de las cadenas
    """

def valida_cadenas(cadena1, cadena2):
    """
    (str),(str)-> (boolean)
    Programa para validar si ambas cadenas esta correspondidas mutuamente

    >>> valida_cadenas("A","T")
    True

    >>> valida_cadenas("A","G")
    False

    >>> valida_cadenas("C","C")
    False

    :param cadena1: Primera cadena ingresada
    :param cadena2: segunda cadena ingresada
    :return: valida si las cadenas son complementarias y retorna booleano
    """

    complemento_total = complemento_base(cadena1)

    valida_corresp = False

    if (complemento_total == cadena2):
        valida_corresp = True

    return valida_corresp
