def calculator(tal1, tecken, tal2, shouldPrint=False, shouldAsk=False):
    if shouldAsk:
        tal1 = float(input("What's your first number: "))
        tecken = input("What operator do you want to use: ")
        while tecken != "+" and tecken != "-" and tecken != "*" and tecken != "/" and tecken != "**" and tecken != "%":
            print("You have to pick one of these operators: + - * / ** %")
            tecken = input("What operator do you want to use: ")
        tal2 = float(input("What's your second number: "))
    if tecken == "+":
        summa = tal1 + tal2
        if shouldPrint:
            print(summa)
        return summa
    elif tecken == "-":
        differens = tal1 - tal2
        if shouldPrint:
            print(differens)
        return differens
    elif tecken == "*":
        produkt = tal1 * tal2
        if shouldPrint:
            print(produkt)
        return produkt
    elif tecken == "/":
        kvot = tal1 / tal2
        if shouldPrint:
            print(kvot)
        return kvot
    elif tecken == "**":
        potens = tal1 ** tal2
        if shouldPrint:
            print(potens)
        return potens
    elif tecken == "%":
        rest = tal1 % tal2
        if shouldPrint:
            print(rest)
        return rest