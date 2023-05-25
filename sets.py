def run():

    print("Métodos:")
    my_list = [1, 1, 1, 4, 534, "asda", (1, 3, "asdsa")]
    my_set = set(my_list)
    print(my_set)
    my_set.pop()
    print(my_set)
    my_set.remove("asda")
    print(my_set)
    my_set.discard("dasaewqñlkwqe")
    print(my_set)
    my_set.add(1)
    print(my_set)
    my_set.update((123 , " asd"))
    print(my_set)
    my_set.clear()

    print("")
    print("Operaciones:")
    set1 = {1, 3, 5, 7, 9, 11}
    print("Set 1: ", set1)
    set2 = {2, 4, 6, 8, 10, 11}
    print("Set 2: ", set2)
    print("Unión: ", set1 | set2)
    print("Intersección: ", set1 & set2)
    print("Diferencia 1 - 2: ", set1 - set2)
    print("Diferencia 2 - 1: ", set2 - set1)
    print("Diferencia simétrica: ", set1 ^ set2)

if __name__ == '__main__':
    run()
