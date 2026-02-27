def getBondPrice_E(face, couponRate, yc):

    cf = face * couponRate
    price = 0
    m = len(yc)

    for t, yt in enumerate(yc, start=1):

        if t == m:
            cashflow = cf + face
        else:
            cashflow = cf

        price += cashflow / (1 + yt)**t

    return price
