def pq_solver():
    import cmath

    # Allow both i and j in input
    p = complex(input("What is p? ").replace('i', 'j'))
    q = complex(input("What is q? ").replace('i', 'j'))

    div = p / 2
    dssr = div**2 - q

    rot = cmath.sqrt(dssr)

    x1 = -div + rot
    x2 = -div - rot

    # Format complex numbers using i instead of j
    def format_complex(z):
        real = z.real
        imag = z.imag

        # If purely real
        if imag == 0:
            return f"{real}"

        # If purely imaginary
        if real == 0:
            return f"{imag}i"

        # Full complex number
        sign = '+' if imag >= 0 else '-'
        return f"{real} {sign} {abs(imag)}i"

    print(f"x1 = {format_complex(x1)}")
    print(f"x2 = {format_complex(x2)}")