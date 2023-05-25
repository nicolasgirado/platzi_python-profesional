# Hola 3 -> HolaHolaHola

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo strings"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Hola"))


if __name__ == "__main__":
    run() 