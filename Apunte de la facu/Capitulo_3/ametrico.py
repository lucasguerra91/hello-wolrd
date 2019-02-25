def main():
    print('Conversor de medidas inglesas a sistema metrico')

    millas = int(input('Ingresar millas :'))
    pies = int(input('Ingresar pies :'))
    pulgadas = int(input('Ingresar pulgadas :'))

    metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
    print('La longitud es de ', metros, 'metros')


main()

