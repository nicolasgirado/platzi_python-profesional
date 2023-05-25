def bordes(func):
    def wrapper(texto):
        print(" " + "_" * (1 + len(texto)))
        print("/" + "_" * (len(texto)) + "/|")
        print("|" + " " * (len(texto)) + "||")
        func("|" + texto + "||")
        print("|" + "_" * (len(texto)) + "|/")

    return wrapper


@bordes
def imprime(texto):
    print(texto)


def run():
    texto = input("Escriba un texto: ")
    imprime(texto)


if __name__ == "__main__":
    run()
