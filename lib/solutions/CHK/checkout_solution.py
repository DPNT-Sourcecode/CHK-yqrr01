

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Docstring ...

    NB: String containing the SKUs of all the products in the basket


    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+

    """
    total = 0
    a = b = c = d = 0

    try:
        for sku in skus:
            # _sku = sku.lower()
            if sku == 'A':
                a += 1
            elif sku == 'B':
                b += 1
            elif sku == 'C':
                c += 1
            elif sku == 'D':
                d += 1
            else:
                total = -1
                raise SyntaxError
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

