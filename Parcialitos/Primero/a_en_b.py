def a_en_b(a, b):
    """
    :param a: lista
    :param b: lista
    :return: True si todos los elementos de A estan en B
    """

    if len(a) > len(b):
        return False

    for i in range(len(a)):
        if a[i] not in b:
            return False

    return True


# ejecucion
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a_en_b(l1, l2))
print(a_en_b(l2, l1))
