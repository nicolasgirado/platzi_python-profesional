def make_division_by(n):
    def make_division(m):
        assert n != 0, "No se permite dividir por cero"
        assert type(n) == int, "Solo se permiten números"
        assert type(m) == int, "Solo se permiten números"
        return m / n
    return make_division

def run():
    division_by_0 = make_division_by(0)
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    print(division_by_5(0))
    print(division_by_3(18))
    print(division_by_5(100))


if __name__ == "__main__":
    run()