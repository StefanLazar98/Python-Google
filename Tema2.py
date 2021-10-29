# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

def my_function(*args, **kwargs):
    if not args:
        return 0

    suma = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            suma += i

    return suma


print(my_function())
print(f"Suma este numerelor reale sau intregi din 1, 5, -3, 'abc', [12, 56, 'cad'] este {my_function(1, 5, -3, 'abc', [12, 56, 'cad'])}")
print(f"Suma este numerelor reale sau intregi din 2, 4, 'abc', param_1=2 este {my_function(2, 4, 'abc', param_1=2)}")


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n]

def recursiv_suma(n1):
    return 0 if n1 == 0 else n1 + recursiv_suma(n1 - 1)


print(f"Suma tuturor numerelor de la [0, n] este {recursiv_suma(5)}")


def recursiv_pare(n2):
    if n2 % 2 == 1:
        return recursiv_pare(n2 - 1)
    return 0 if n2 == 0 else n2 + recursiv_pare(n2 - 2)


print(f"Suma numerelor pare de la [0, n] este {recursiv_pare(5)}")


def recursiv_impare(n3):
    if n3 % 2 == 0:
        return recursiv_impare(n3 - 1)
    return 1 if n3 == 1 else n3 + recursiv_impare(n3 - 2)


print(f"Suma numerelor impare de la [0, n] este {recursiv_impare(5)}")


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.

def intreg(n4):
    try:
        val = int(n4)
    except ValueError:
        return 0
    return val


n5 = input("Input: ")
print(f"Output: {intreg(n5)}")
