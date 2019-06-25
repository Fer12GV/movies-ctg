from unittest import TestCase


# Function to identify a bouncy number

def bouncy(N):
    cociente = int(N)
    Arr = []  # I create the list
    n = 0
    m = 0
    # Added items to the list
    while cociente >= 10:
        num = cociente % 10
        Arr.insert(0, num)
        cociente = cociente // 10
    Arr.insert(0, cociente)

    # Compare items in the list and validate a bouncy number as true
    x = len(Arr) - 1
    for i in range(x):
        if Arr[i] >= Arr[i + 1]:
            n += 1
            if Arr[i] == Arr[i + 1]:
                m += 1
        else:
            m += 1
    if m == x or n == x:
        return False
    else:
        return True


# Function Input of the percentage value


def validarPorcentaje(percentage_value):
    porcentage = percentage_value
    if porcentage < 0:
        raise TypeError("NO ES CORRECTO UN VALOR NEGATIVO PARA EL PORCENTAJE")
    return porcentage


# EXIT AND CONTROL OF EXCEPTIONS FOR THE INCOME OF SECURITIES


def entry_percentages(percentage_value):
    while True:
        try:
            P = validarPorcentaje(percentage_value)
            break
        except TypeError as ErrorDeNumeroNegativo:
            print(ErrorDeNumeroNegativo)
            break
        except ValueError:
            print("EL TIPO DE DATO INTRODUCIDO NO ES EL CORRECTO")
    # DETERMINATION OF THE MINIMUM NUMBER FOR A PERCENTAGE OF BOUNCY NUMBERS
    number = 101
    percentage = 0
    quantity = 0
    while percentage < P:
        if bouncy(number):
            quantity += 1
        percentage = (quantity / number) * 100
        number += 1
    #print("Número mínimo donde la proporción de números bouncy es excatamente al " + str(P) + "%" + " : " + str(number-1))
    return number-1

# ---------- MAIN ------------------  TEST ---------------------------------

class PercentageBouncyNumberTestCase(TestCase):

    def test_bouncy_function_should_return_true_for_101(self):
        assert bouncy(101)

    def test_bouncy_function_should_return_false_for_7110(self):
        assert not bouncy(7110)

    def test_entry_percentage_function_should_return_minimum_number_bouncy_for_50(self):
        assert entry_percentages(20)

    def test_entry_porcentaje_fucntion_return_1587000_for_99(self):
        self.assertEqual(entry_percentages(99), 1587000)

    def test_entry_porcentaje_fucntion_return_1587000_for_99(self):
        self.assertEqual(entry_percentages(50), 538)

