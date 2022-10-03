import math

def compare(message):
    #присвоєння значень
    a, weight1, price1, weight2, price2 = map(str, message.text.split()) #reading of variables
    weight1 = float(weight1)
    price1 = float(price1)
    weight2 = float(weight2)
    price2 = float(price2)

    # calculation of compare
    one = price1 / (weight1 / 1000)
    two = price2 / (weight2 / 1000)

    if int(one) == one:
        one = int(one)
    else:
        one = round(one, 2)
    if int(two) == two:
        two = int(two)
    else:
        two = round(two, 2)

    return f"""Ціна першого товару {one} грн/кг або грн/літр
Ціна другого товару {two} грн/кг або грн/літр"""
