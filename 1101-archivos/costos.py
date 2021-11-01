def calcular_punto_equilibrio(cf, pv, cvu):
    return cf / (pv - cvu)


def calcular_utilidad(pv, uv, cf, cvu):
    return (pv * uv) - cf - (cvu * uv)



costo_fijo = eval(input("Escribe el costo fijo: "))
precio_venta = eval(input("Escribe el precio de venta: "))
costo_variable_unitario = eval(input("Escribe el costo variable unitario: "))
unidades_vendidas = eval(input("Escribe las unidades vendidas por mes: "))


#punto_equilibrio = costo_fijo / ( precio_venta - costo_variable_unitario)
punto_equilibrio = calcular_punto_equilibrio(costo_fijo, precio_venta, costo_variable_unitario)

print("El punto de elquibro en unidades es:", punto_equilibrio)

#a) Los costos variables disminuyen 10 por ciento.
punto_equilibrio = calcular_punto_equilibrio(costo_fijo, precio_venta, costo_variable_unitario * 0.9)
print("El punto de elquibro en unidades de (a) es:", punto_equilibrio)

#b) Los costos fijos disminuyen 8 por ciento.

punto_equilibrio = calcular_punto_equilibrio(costo_fijo * 0.92, precio_venta, costo_variable_unitario)
print("El punto de elquibro en unidades de (b) es:", punto_equilibrio)


#c) El precio por pizza aumenta a $110.

punto_equilibrio = calcular_punto_equilibrio(costo_fijo, 110, costo_variable_unitario)
print("El punto de elquibro en unidades de (c) es:", punto_equilibrio)


#utilidad_regular = (precio_venta * unidades_vendidas) - costo_fijo - (costo_variable_unitario * unidades_vendidas)
utilidad_regular = calcular_utilidad(precio_venta,unidades_vendidas, costo_fijo, costo_variable_unitario)
print("Utilidad regular es:", utilidad_regular)

#utilidad_regular = (precio_venta * (unidades_vendidas * 1.15)) - (costo_fijo+3000) - (costo_variable_unitario * (unidades_vendidas*1.15))
utilidad_regular = calcular_utilidad(precio_venta, unidades_vendidas*1.15, costo_fijo+3000, costo_variable_unitario)
print("Utilidad regular modificada es:", utilidad_regular)
