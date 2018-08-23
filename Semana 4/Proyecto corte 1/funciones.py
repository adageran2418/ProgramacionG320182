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
    pass


def calcular_precio_servicio_extras(cantidad_horas):
    pass


def calcular_costo_envio(kilometros):
    pass

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    pass


def calcular_iva_producto(coste_producto, tasa):
    pass


def calcular_iva_servicio(cantidad_horas, tasa):
    pass


def calcular_iva_envio(kilometros, tasa):
    pass


def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    pass


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    pass

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    pass
