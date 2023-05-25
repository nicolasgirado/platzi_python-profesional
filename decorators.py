from datetime import datetime


def excecution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper


@excecution_time
def random_func():
    for _ in range(1, 100000000):
        pass
    print("Fin random function")

@excecution_time
def suma(a: int, b: int) -> int:
    print(str(a) + "+" + str(b) + " es igual a " + str(a + b))


@excecution_time
def saludo(nombre="Cesar"):
    print("Hola", nombre)


def run():
    random_func()
    suma(1, 2)
    saludo()


if __name__ == "__main__":
    run()
