def diferencia_vectores(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x, dif_y, dif_z = x1 - x2, y1 - y2, z1 - z2
    return dif_x, dif_y, dif_z


def calcula_producto_cruz(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    rx, ry, rz = y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2
    return rx, ry, rz


def calcula_norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5


def calcula_area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    abx, aby, abz = diferencia_vectores(x2, y2, z2, x1, y1, z1)
    acx, acy, acz = diferencia_vectores(x3, y3, z3, x1, y1, z1)
    pcx, pcy, pcz = calcula_producto_cruz(abx, aby, abz, acx, acy, acz)
    area = calcula_norma(pcx, pcy, pcz) / 2
    return area


print(calcula_norma(3, 2, -4))
print(diferencia_vectores(8, 7, -3, 5, 3, 2))
print(calcula_producto_cruz(1, 4, -2, 3, -1, 0))
print(calcula_area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))
