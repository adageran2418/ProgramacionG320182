def calcular_precio_producto(coste_producto):
    '''
    (float) -> float
    Calcula el precio de un producto sumandole una comision del 50% sobre el costo del producto
    >>> calcular_precio_producto(100)
    150.0
    >>> calcular_precio_producto(200)
    300.0
    >>> calcular_precio_producto(500)
    750.0
    :param coste_producto: (num) El costo del producto
    :return: (num) El costo del producto màs el 50%
    '''
    precio_producto = coste_producto + (coste_producto/2)
    return precio_producto

    # Llamar la funcion
precio_producto = calcular_precio_producto (float(input('Digite el coste del producto')))

     #Imprimir coste del producto
print('El costo del producto es', precio_producto)


def calcular_precio_servicio(cantidad_horas):
    '''
    (float) -> float
    Calcula el precio del servicio sumando la tarifa por hora
    >>> calcular_precio_servicio(2)
    200000
    >>> calcular_precio_servicio(45)
    4500000
    >>> calcular_precio_servicio(4)
    400000
    :param cantidad_horas: (num) El numero de horas trabajado
    :return: (num) el precio del servicio
    '''
    precio_servicio = cantidad_horas * 100000
    return precio_servicio

# Llamar la funcion
precio_servicio = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

# Imprimir el precio del servicio
print('el precio del servicio es', precio_servicio)


def calcular_precio_servicio_extras(cantidad_horas):
    '''
    (float) - > float
    Calcula el precio de las horas extra
    >>> calcular_precio_servicio_extras(1)
    125000.0
    >>> calcular_precio_servicio_extras(4)
    500000.0
    >>> calcular_precio_servicio_extras(8)
    1000000.0
    :param cantidad_horas: (num) cantidad de horas extras trabajadas
    :return: (num) precio de sevicio con horas extras
    '''

    # Calcular el precio del servicio con horas extras

    precio_servicio_extras = calcular_precio_servicio(cantidad_horas)+(calcular_precio_servicio(cantidad_horas)*0.25)
    return precio_servicio_extras

    # Llamar la funcion
precio_servicio_extras = calcular_precio_servicio_extras (float(input('Digite la cantidad de horas extras')))

# Imprimir El precio del servicio con horas extras
print ('El precio del servicio con horas extras es',precio_servicio_extras)


def calcular_costo_envio(kilometros):
    '''
    (float) -> float
    Calcula el costo del envio teniendo en cuenta el recargo por kilometro
    >>> calcular_costo_envio(3)
    345
    >>> calcular_costo_envio(5)
    575
    >>> calcular_costo_envio(10)
    1150
    :param kilometros: (num) Cantidad de kilometros del envio
    :return: (num) El costo del envio
    '''
    costo_envio = kilometros * 115
    return costo_envio

# Llamar la funcion
costo_envio = calcular_costo_envio (float(input('Digite la cantidad de kilometros del envio')))

# Imprimir el costo del envio
print('El costo del envio es',costo_envio)

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    '''
    (float) -> float
    Calcula el precio de un producto vendido afuera teniendo en cuenta el costo del envio
    >>> calcular_precio_producto_fuera(100,10)
    1300.0
    >>> calcular_precio_producto_fuera(200,10)
    1450.0
    >>> calcular_precio_producto_fuera(400,10)
    1750.0
    :param coste_producto: (num) valor del producto
    :param kilometros: (num) kilometros del envio
    :return: (num) costo del valor del producto mas el valor del envío
    '''

    precio_producto_fuera = calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)
    return precio_producto_fuera

# Llamar la funcion
precio_producto_fuera = calcular_precio_producto_fuera(float(input('Digite el coste del producto')),
                                                       float(input('Digite la cantidad de kilometros del envio')))

# Imprimir el precio el producto mas el costo del envio
print ('El precio del producto mas el envio es', precio_producto_fuera)


def calcular_iva_producto(coste_producto, tasa):
    '''
    (float) - > float
    Calcula el iva del producto
    >>> calcular_iva_producto(200, 19)
    57.0
    >>> calcular_iva_producto(500, 10)
    75.0
    >>> calcular_iva_producto(8000, 4)
    480.0
    :param coste_producto: (num) Costo del producto
    :param tasa: (num) valor de la tasa (entre 0 y 100)
    :return: (num) Valor iva del producto
    '''

    valor_iva_producto = (calcular_precio_producto(coste_producto)*tasa/100)
    return valor_iva_producto

# Llamar la funcion
valor_iva_producto = calcular_iva_producto (float(input('digite valor producto ')),
                                            float(input('digite su Tasa ')))

# Imprimir el iva del producto
print('El iva del producto es', valor_iva_producto)

def calcular_iva_servicio(cantidad_horas, tasa):
    '''
    (float) - > float
    Calcula el iva del servicio
    >>> calcular_iva_servicio(2, 7)
    14000.0
    >>> calcular_iva_servicio(5, 15)
    75000.0
    >>> calcular_iva_servicio(8, 30)
    240000.0
    :param cantidad_horas: (num) Cantidad de horas trabajadas
    :param tasa: (num) valor de la tasa
    :return: (num) valor iva del servicio
    '''
    valor_iva_servicio = (calcular_precio_servicio(cantidad_horas)*tasa/100)
    return valor_iva_servicio

# Llamar la funcion

valor_iva_servicio = calcular_iva_servicio(float(input('Digite la cantidad de horas')),
                                           float (input('Digite su Tasa')))

# Imprimir el iva del servicio
print('El iva del serevicio es', valor_iva_servicio)

def calcular_iva_envio(kilometros, tasa):
    '''
    (float) - > float
    Calcula el valor del iva del envio
    >>> calcular_iva_envio(3, 50)
    172.5
    >>> calcular_iva_envio(10, 2)
    23.0
    >>> calcular_iva_envio(6000, 90)
    621000.0
    :param kilometros: (num) Cantidad de kilometros de envio
    :param tasa: (num) Valor de la tasa
    :return: (num) Valor del iva del envio
    '''
    valor_iva_envio = (calcular_costo_envio(kilometros)* tasa/100 )

    return valor_iva_envio

# llamar la funcion

valor_iva_envio = calcular_iva_envio(float(input('Digite los kilometros')),
                                           float (input('Digite su Tasa')))

# Imprimir el iva del envio
print('El iva del envio es', valor_iva_envio)



def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    '''
    (float) -> float
    Calcula el iva de un servicio fuera
    >>> calcular_iva_servicio_fuera(10,19)
    237500.0
    >>> calcular_iva_servicio_fuera(12,25)
    375000.0
    >>> calcular_iva_servicio_fuera(5,25)
    156250.0
    :param cantidad_horas: Cantidad de horas del servicio
    :param tasa: Impuesto de la tasa
    :return: valor de la tasa sobre el envio
    '''
    iva_servicio = (calcular_precio_servicio(cantidad_horas)*tasa/100)

# llamar la funcion

iva_servicio = calcular_iva_servicio_fuera(float(input("Digite la cantidad de Horas")),
                                           float(input("Ingrese la tasa")))

#imprimir el iva del servicio

print("El iva del servicio es: ", iva_servicio)


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    '''
    (float) -> float
    >>> calcular_recaudo_locales (100, 200, 300)
    900.0
    >>> calcular_recaudo_locales (1000, 2000, 3000)
    9000.0
    >>> calcular_recaudo_locales (666, 999, 777)
    3663.0
    :param coste_producto_1: (num) costo del producto 1
    :param coste_producto_2: (num) costo del producto 2
    :param coste_producto_3: (num) costo del producto 3
    :return: (num) Recaudo costo productos locales
    '''
    recaudo_local = calcular_precio_producto(coste_producto_1)+calcular_precio_producto(coste_producto_2)+calcular_precio_producto(coste_producto_3)
    return recaudo_local

# Llamar la funcion 3 veces

coste_producto_1 = calcular_precio_producto(float(input('digite coste del producto 1 ')))

coste_producto_2 = calcular_precio_producto(float(input('digite coste del producto 2 ')))

coste_producto_3 = calcular_precio_producto(float(input('digite coste del producto 3 ')))


# Calcular recaudo coste de productos locales
recaudo_productos = coste_producto_1 + coste_producto_2 + coste_producto_3


#Imprimir el recaudo de los productos
print ('El recaudo total de los productos es ', recaudo_productos)

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    '''
    (float,float,float,float) - > float
    >>> calcular_recaudo_horas_extra(2,2,2,2)
    1000000.0
    >>> calcular_recaudo_horas_extra(1,1,1,1)
    500000.0
    >>> calcular_recaudo_horas_extra(4,4,4,4)
    2000000.0
    :param horas_1: Horas extra 1
    :param horas_2: Horas extra 2
    :param horas_3: Horas extra 3
    :param horas_4: Horas extra 4
    :return:valor total de las horas extras solicitadas

    '''

    recaudo_horas_extra = calcular_precio_servicio(horas_1)+calcular_precio_servicio(horas_2)+calcular_precio_servicio(horas_3)+calcular_precio_servicio(horas_4)
    return recaudo_horas_extra

# llamar la funcion cuatro veces

horas_1 = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

horas_2 = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

horas_3 = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

horas_4 = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

# Calcular recaudo horas extra

recaudo_horas_extra = horas_1 + horas_2 + horas_3 + horas_4

# Imprimir el recaudo de las horas extra

print ('El recaudo de las horas extra es ', recaudo_horas_extra)

def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    '''
    (float,float,float,float) - > float
    >>> calcular_recaudo_horas_extra(100,200,2,2)
    4450.0
    >>> calcular_recaudo_horas_extra(200,300,1,5)
    6750.0
    >>> calcular_recaudo_horas_extra(500,1000,4,3)
    9251.0
    :param coste_producto_1: Horas extra 1
    :param coste_producto_2: Horas extra 2
    :param horas_1: Horas extra 3
    :param horas_2: Horas extra 4
    :return:valor del recaudo mixto

    '''
    recaudo_mixto_local = calcular_precio_producto(coste_producto_1)+calcular_precio_producto(coste_producto_2)+calcular_precio_servicio(horas_1)+calcular_precio_servicio(horas_2)
    return recaudo_mixto_local

# Llamar la funcion cuatro veces

coste_producto_1 = calcular_precio_producto(float(input('digite coste del producto 1 ')))

coste_producto_2 = calcular_precio_producto(float(input('digite coste del producto 2 ')))

horas_1 = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

horas_2 = calcular_precio_servicio(float(input('Digite la cantidad de horas')))

# Calcular recaudo mixto

recaudo_mixto_local = coste_producto_1 + coste_producto_2 + horas_1 + horas_2

# Imprimir el recaudo mixto
print ('El recaudo mixto local es ', recaudo_mixto_local)


