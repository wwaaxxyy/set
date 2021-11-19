# Programme en ligne de commande qui dit si un ensemble de cartes est un set
from rich import print
from rich.console import Console
import random

console = Console()


colors = {'red':1, 'green':2, 'violet':3}
numbers = {'one':1, 'two':2, 'three':3}
shapes = {'oval':1, 'diamond':2, 'peanut':3}
fills = {'empty':1, 'full':2, 'hatched':3}


def random_card():
    color = get_key(colors,random.randint(1,3))
    shape = get_key(shapes,random.randint(1,3))
    fill = get_key(fills,random.randint(1,3))
    number = get_key(numbers,random.randint(1,3))
    card = {'color':color, 'shape':shape, 'fill':fill, 'number':number}
    return card


def is_set(card1, card2, card3):
    resultSet = False
    c = (colors[card1['color']] + colors[card2['color']] + colors[card3['color']]) % 3 
    n = (numbers[card1['number']] + numbers[card2['number']] + numbers[card3['number']]) % 3 
    s = (shapes[card1['shape']] + shapes[card2['shape']] + shapes[card3['shape']]) % 3 
    f = (fills[card1['fill']] + fills[card2['fill']] + fills[card3['fill']]) % 3 

    if (c+f+s+n) == 0 :
        resultSet = True
    return resultSet

"""     else:
        if c != 0 : print("Couleur")
        if n != 0 : print("Nombre")
        if s != 0 : print("Forme")
        if f != 0 : print("Remplissage")
 """


def get_key(dico, value):
    return list(dico.keys())[list(dico.values()).index(value)]

def tirage(tries):
    for i in range(tries):
        c1 = random_card()
        c2 = random_card()
        c3 = random_card()

        
        if (is_set(c1,c2,c3)):
            print("**** tada we found a set *****")
            print(c1,c2,c3)
        else:
            print("sad trombone.wav")

def find_set(tries):
    c1 = random_card()
    c2 = random_card()
    c3 = random_card()
    if (is_set(c1,c2,c3)):
        print("**** tada we found a set *****", tries)
        print(c1,c2,c3)
    else:
        find_set(tries+1)


try:
    find_set(1)
    card4 = {'color': 'red', 'shape': 'peanut', 'fill': 'empty', 'number': 'one'}
    card5 = {'color': 'red', 'shape': 'peanut', 'fill': 'full', 'number': 'two'}
    card6 = {'color': 'red', 'shape': 'peanut', 'fill': 'hatched', 'number': 'three'}

    #print(card4, card5, card6)
    #print(is_set(card4,card5, card6)) 

except Exception:
    print(":bomb: t'as pas oublié un  [bold magenta]Truc[/bold magenta]")
    console.print_exception(show_locals=True)