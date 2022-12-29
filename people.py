import csv

# On crée une liste vide pour stocker les dictionnaires de personnes
people = []

# On Ouvre le fichier CSV en mode lecture
with open('people.csv', 'r') as file:
  # On crée un lecteur CSV
  reader = csv.reader(file)
  for row in reader:
    # On crée un dictionnaire pour la personne avec les informations de la ligne
    person = {
      'nom': row[0],
      'prenom': row[1],
      'age': row[2],
      'ville': row[3]
    }
    # On ajoute le dictionnaire de la personne à la liste des personnes
    people.append(person)

# Fonction pour afficher la liste des personnes
def print_people():
  for person in people:
    # On affiche les informations de la personne
    print(f"{person['nom']} {person['prenom']}, {person['age']} ans, {person['ville']}")

# On ajoute une nouvelle personne
def add_person():
  nom = input("Entrez le nom : ")
  prenom = input("Entrez le prénom : ")
  age = input("Entrez l'âge : ")
  ville = input("Entrez la ville : ")

  # On crée un dictionnaire pour la nouvelle personne avec les informations saisies
  person = {
    'nom': nom,
    'prenom': prenom,
    'age': age,
    'ville': ville
  }

  people.append(person)

# Fonction pour modifier les informations d'une personne
def update_person():

  # Demander à l'utilisateur de saisir le nom de la personne à modifier
  name = input("Entrez le nom de la personne à modifier : ")
  for person in people:
    # Si le nom de la personne correspond au nom saisi :
    if person['nom'] == name:

      person['nom'] = input("Entrez le nouveau nom : ")
      person['prenom'] = input("Entrez le nouveau prénom : ")
      person['age'] = input("Entrez le nouvel âge : ")
      person['ville'] = input("Entrez la nouvelle ville : ")

      # Afficher un message indiquant que les informations ont été mises à jour:
      print("Les informations ont été modifiées.")
      return
  # Si aucune personne n'a été trouvée avec le nom saisi, afficher le message d'erreur suivant :
  print("Aucune personne n'a été trouvée avec ce nom.")

# Fonction pour supprimer une personne ( Attention à la majuscule)
def delete_person():
  name = input("Entrez le nom de la personne à supprimer : ")
  for person in people:
    # Si le nom de la personne correspond au nom saisi :
    if person['nom'] == name:
      # Supprimer la personne de la liste
      people.remove(person)
      # Sortir de la boucle une fois que la personne a été supprimée
      break

# Afficher le menu:
while True:
  print("1. Afficher la liste de toutes les personnes")
  print("2. Ajouter une nouvelle personne")
  print("3. Modifier les informations d'une personne")
  print("4. Supprimer une personne")
  print("5. Quitter")
  # Demander à l'utilisateur de choisir une option
  choice = int(input("Choisissez une option : "))
  # Selon l'option choisie...
  if choice == 1:
    # Afficher la liste des personnes
    print_people()
  elif choice == 2:
    # Ajouter une nouvelle personne
    add_person()
  elif choice == 3:
    # Modifier les informations d'une personne
    update_person()
  elif choice == 4:
    # Supprimer une personne
    delete_person()
  elif choice == 5:
    # Quitter le programme
    break
  else:
    # Afficher un message d'erreur si l'option choisie est incorrecte
    print("Option incorrecte")
