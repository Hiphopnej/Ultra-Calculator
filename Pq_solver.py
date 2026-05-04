def pq_solver():
    from Calculator import calculator
    from Square_root_calculator import square_root
    p = float(input("What is p? "))
    q = float(input("What is q? "))
    # Example for imaganary numbers x = 3 + 2.j
    # There exists a data type called complex
    # Will try to add in the future
    div = calculator(p, "/", 2)
    div_med_upphöjt = calculator(div, "**", 2)
    dssr = calculator(div_med_upphöjt, "-", q)
    if dssr < 0:
        dssr = abs(dssr)
        rot = square_root(dssr, 2)
        print(f"x1 = {-div} + {rot}i and x2 = {-div} - {rot}i")
    else:
        rot = square_root(dssr, 2)
        x1 = -div + rot
        x2 = -div - rot
        print(f"x1 = {x1} and x2 = {x2}")