def pytagoras_solver():
    from Calculator import calculator
    from Square_root_calculator import square_root
    Vad_ska_beräknas = input("Vad ska beräknas a, b, c ")
    if Vad_ska_beräknas == "c":
        a = float(input("Vad är den närliggande kateten(a) "))
        b = float(input("Vad är den motstående kateten(b) "))
        a = calculator(a, "**", 2)
        b = calculator(b, "**", 2)
        c = calculator(a, "+", b)
        c = square_root(c, 2)
        print(f"c är {c}")
    elif Vad_ska_beräknas == "a":
        b = float(input("Vad är den motstående kateten(b) "))
        c = float(input("Vad är hypotenusan(c) "))
        b = calculator(b, "**", 2)
        c = calculator(c, "**", 2)
        a = calculator(c, "-", b)
        a = square_root(a,2)
        print(f"a är {a}")
    elif Vad_ska_beräknas == "b":
        a = float(input("Vad är den närliggande kateten(a) "))
        c = float(input("Vad är hypotenusan(c) "))
        a = calculator(a, "**", 2)
        c = calculator(c, "**", 2)
        b = calculator(c, "-", a)
        b = square_root(b, 2)
        print(f"b är {b}")