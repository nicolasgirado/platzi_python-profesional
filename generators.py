import time


# def fibo_gen(max):
#     n1 = 0
#     n2 = 1
#     counter = 0
#     while True:
#         if counter == 0:
#             counter += 1
#             yield n1
#         elif counter == 1:
#             counter += 1
#             yield n2
#         else:
#             aux = n1 + n2
#             if not max or aux <= max:
#                 n1, n2 = n2, aux
#                 counter += 1
#                 yield aux
#             else:
#                 raise StopIteration


# def run():
#     max = input("Ingrese un máximo: ")
#     assert max == "" or (max.isnumeric() and int(
#         max)) != 0, "Sólo se permiten enteros positivos, o presione enter para no ingresar un máximo"
#     if max.isnumeric():
#         max = int(max)
#     fibonacci = fibo_gen(max)
#     for element in fibonacci:
#         print(element)
#         time.sleep(1)


# if __name__ == '__main__':
#     run()


def fibo_gen(max=None):
    n1, n2 = 0, 1
    while not max or max >= n1:
        yield n1
        n1, n2 = n2, n1 + n2


if __name__ == '__main__':
    Fibonacci = fibo_gen(4)
    for element in Fibonacci:
        print(element)
        time.sleep(1)
