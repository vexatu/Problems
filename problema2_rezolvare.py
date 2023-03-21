"""Exercițiul 2 Scrie o funcție numită print_kwargs(**kwargs) care afișează toate perechile cheie-valoare
din dicționarul kwargs.
Cerințe
• Funcția trebuie să accepte orice număr de argumente cu nume (cheie-valoare)
• Funcția trebuie să afișeze toate perechile cheie-valoare din dicționarul kwargs
"""

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        result = print(key, value)
    return result
print_kwargs(first_name = "Jhon" , middle_name = "Luke", age = 30 )