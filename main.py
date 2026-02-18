import random

objets = [
    "des pâtes",
    "une pizza froide",
    "un kebab douteux"
]

sujets = [
    "Aujourd’hui je mange",
    "Ce soir je commande",
    "Demain je cuisine"
]

raisons = [
    "parce que la vie est dure",
    "parce que j’ai la flemme",
    "parce que c’est gratuit"
]

print(random.choice(sujets),
      random.choice(objets),
      random.choice(raisons))


