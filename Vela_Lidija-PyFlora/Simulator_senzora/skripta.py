import random


def generiraj(pocetni, krajnji):
    return random.randint(pocetni,krajnji)


def generiraj_sve_podatke():
    temperatura = generiraj(25, 37)
    vlaznost = generiraj(40, 100)
    ph = generiraj(1, 14)
    salinitet = generiraj(1, 20)
    svjetlina = generiraj(1, 100)
    return [
        temperatura,
        vlaznost,
        ph,
        salinitet,
        svjetlina
    ]


if __name__ == '__main__':
    print(generiraj_sve_podatke())