# Programme en ligne de commande qui dit si un ensemble de cartes est un set
from rich import print
from rich.console import Console
console = Console()

def is_set(number):
    if number is not 3:
        return False
    else:
        return True

try:
    print("c'est set? ", is_set())
except Exception:
    print(":bomb: t'as pas oublié un  [bold magenta]Truc[/bold magenta]")
    console.print_exception(show_locals=True)