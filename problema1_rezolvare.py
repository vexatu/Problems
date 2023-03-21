"""Exercițiul 1
Scrie o funcție numită sum_args(*args) care returnează suma tuturor argumentelor primite.
Cerințe
• Funcția trebuie să accepte orice număr de argumente numere întregi sau zecimale
• Funcția trebuie să returneze suma tuturor argumentelor primite"""

def sum_args(*args):
    sum_all = 0
    for numbers in args:
        sum_all += numbers
    return sum_all
print(sum_args(2, 2.23))