"""Exercițiul 3
Scrieți o funcție numită process_data(func, *args, **kwargs) care primește ca parametru o funcție func
și orice număr de argumente în formă de tuple *args și keyword arguments **kwargs. Funcția trebuie să
execute funcția func cu argumentele din *args și **kwargs și să returneze rezultatul.
Cerințe
• Funcția trebuie să accepte o funcție ca primul parametru și orice număr de argumente în formă
de tuple *args și keyword arguments **kwargs.
• Funcția trebuie să execute funcția func cu argumentele din *args și **kwargs și să returneze
rezultatul."""

def process_data(func, *args, **kwargs):
    return func(*args, **kwargs)
def add(a,b):
    return a+b
def mul(a,b,c):
    return a*b*c

print(process_data(add,1,2))
print(process_data(mul,1,2,3))