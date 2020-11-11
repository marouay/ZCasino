# Module pour générer un nombre aléatoire
import os
import random
# Module pour arrondir un float
from math import ceil


def main(choix: int, mise: int):
    """
    Jeu de roulette numérique
    :param choix: Numéro choisi par le client
    :param mise: Somme misée par le client
    :return: Valeur gagné
    """

    #  Affichage des variables du jeux
    print("le choix du client est le nombre :", choix)
    print("la mise du client est la somme :", mise, "$")

    roulette_chance: int = random.randrange(50)
    print("Le nombre gagné est :", roulette_chance)

    # Si le client gagne:
    # 1) choix = roulette
    if (roulette_chance == choix):
        gain = mise + 3 * mise
    # 2) choix et roulette de même couleur (pair ou impair):
    elif (roulette_chance % 2 == choix % 2):
        gain = mise + ceil(mise / 2)
    # Le cas perdant:
    else:
        gain = 0

    print("Le client à gagné une somme de :", gain, "$")
    return gain

def saisie_choix() -> int:
    """
    Tester le choix du client
    :return: un entier entre 0 et 49
    """
    choix_mise = -1
    erreur_saisie: bool = True
    while erreur_saisie:
        try:
            choix_mise = int(input("Le choix du client est : "))
            assert 49 >= choix_mise >= 0
            erreur_saisie = False
        except ValueError:
            print("Le nombre n'est pas entier")
        except AssertionError:
            print("Le nombre n'appartient pas à l'interval [0, 49]")
    return choix_mise


def saisie_mise(argent : int) -> int:
    """
    Tester le choix du client
    :return: un entier entre 0 et 49
    """
    mise = -1
    erreur_saisie: bool = True
    while erreur_saisie:
        try:
            mise = int(input("La mise du client est : "))
            assert mise > 0, 'la mise doit être strictement positif'
            assert mise <= argent, 'la mise doit être inférieur ou égale à l\'argent total du client ' + str(argent)
            erreur_saisie = False
        except ValueError as error:
            print("La mise n'est pas entier")
        except AssertionError as error:
            print(error)
    return mise


argent = 1000
jouer_encore = True

while argent > 0 and jouer_encore :
    choix_mise = saisie_choix()
    mise = saisie_mise(argent)
    argent -= mise
    # Lancement de la fonction jeux de roulette
    argent += main(choix_mise, mise)

    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        jouer_encore = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", argent, "$")
        quitter = input("Souhaitez-vous continuer de jouer (o/n) ? ")
        if quitter == "n" or quitter == "N":
            print("Vous quittez le casino avec vos gains.")
            jouer_encore = False

# On met en pause le système (Windows)
os.system("pause")
