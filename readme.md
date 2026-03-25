# 🔴 Neurone Rouge

Un perceptron à un seul neurone capable de détecter si une couleur est rouge ou non, avec apprentissage en temps réel via feedback utilisateur.

## Lancer le projet

```bash
pip install flask
python main.py
```

Puis ouvrir [http://localhost:5000](http://localhost:5000).

## Utilisation

À chaque chargement de page, une couleur aléatoire est générée et le neurone prédit si elle est rouge ou non. 

Deux boutons permettent de donner un feedback :
- **D'accord** : la prédiction était correcte, rien ne change
- **Pas d'accord** : la prédiction était fausse

Quand on clique sur **Pas d'accord**, la couleur et le label correct sont ajoutés aux données d'entraînement, puis le neurone se réentraîne automatiquement sur l'ensemble du jeu de données mis à jour. Le modèle converge en général en quelques dizaines d'itérations.

Les données d'entraînement et l'état du neurone sont sauvegardés entre les sessions dans `data/`.

## Comment ça marche

Chaque couleur `(R, G, B)` est un point dans un espace 3D. Le neurone apprend un vecteur `p = [p₁, p₂, p₃]` qui définit un plan séparateur :

```
p₁·R + p₂·G + p₃·B = 1
```

Si le produit est **≥ 1**, la couleur est rouge. Sinon, elle ne l'est pas. L'apprentissage ajuste ce plan à chaque feedback via la règle du Perceptron.
