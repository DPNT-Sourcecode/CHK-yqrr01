

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Docstring ...

    NB: String containing the SKUs of all the products in the basket
    """
    total = 0
    a = b = c = d = 0

    try:
        for sku in skus:
            _sku = sku.lower()
            if _sku == 'a':
                a += 1
            if _sku == 'b':
                b += 1
            if _sku == 'c':
                c += 1
            if _sku == 'd':
                d += 1
            else:
                total = -1
                break
    # TODO: attr error
    except SyntaxError as ex:
        total = -1
        print(str(ex))
    else:
        total += (a / 3)*130 + (a % 3)*50
        total += (b / 2)*45 + (b % 2)*30
        total += c*20
        total += d*15

    return total






