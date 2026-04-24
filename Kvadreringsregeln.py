def kvadreringsregeln(tal1, tal2, shouldPrint=False, shouldAsk=False):
    if shouldAsk:
        tal1 = input("Vad är ditt första tal")
        tal2 = input("Vad är ditt andra tal")
    
    if "x" in tal1 or "x" in tal2:
        print("Test")

kvadreringsregeln("2", "x**2")