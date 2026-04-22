def pq_solver():
    from Calculator import calculator
    from Square_root_calculator import square_root
    p = float(input("Vad är p? "))
    q = float(input("Vad är q? "))
    # exempel på hur man skriver imaginära tal x = 3 + 2.j
    # finns en datatyp som heter complex
    div = calculator(p, "/", 2)
    div_med_upphöjt = calculator(div, "**", 2)
    dssr = calculator(div_med_upphöjt, "-", q)
    if dssr < 0:
        dssr = abs(dssr)
        rot = square_root(dssr, 2)
        print(f"x1 = {-div} + {rot}i och x2 = {-div} - {rot}i")
    else:
        rot = square_root(dssr, 2)
        x1 = -div + rot
        x2 = -div - rot
        print(f"x1 = {x1} och x2 = {x2}")