

# Menu
        

def print_menu():
    print("1. Lancer le jeu")
    print("2. Voir l'historique")
    print("3. Quitter le jeu")

# Recuperer choix utiisateur
#       Lancer la bonne option
#  

def recuperer_nombre_valide(min_val, max_val, message):
    saisie = input("Entrez votre choix : ")
    while (saisie > 1) and (saisie < 3):
     return saisie

def main():
    recuperer_nombre_valide(1,5,"Choisir une options")
