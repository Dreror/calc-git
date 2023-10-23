def add(x, y):
    return x + y


def dis(x, y):
    return x - y


def mul(x, y):
    return x * y


def dell(x, y):
    return x / y


def sqr(x, y):
    return x ** y


def qua(x):
    return x ** 2


def qb(x):
    return x ** 3


print("Вас вітає калькулятор!")
a = 1
while a in range(0, 8):
    print("Доступні функції:",
          "1 - додавання",
          "2 - віднімання",
          "3 - множення",
          "4 - ділення",
          "5 - взведення в ступінь",
          "6 - зведення до квадрата",
          "7 - зведення до куба",
          "0 - Вийти", sep="\n")
    a = int(input("Що бажаете зробити? = "))
    while a not in range(0, 8):
        print("Невірне значення! Спробуйте ще раз")
        a = int(input("Що бажаете зробити? = "))
