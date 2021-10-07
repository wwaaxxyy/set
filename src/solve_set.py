# Programme en ligne de commande qui dit si un ensemble de cartes est un set
import traceback

def is_set(number):
    if number is not 3:
        return False
    else:
        return True

try:
    print("c'est set? ", is_set())
except Exception:
    #traceback.print_stack()
    print("t'as pas oublié un truc")