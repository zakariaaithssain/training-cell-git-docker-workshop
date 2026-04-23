# Guide de l'Étudiant : Comment créer votre Magasin 🛒

Bienvenue dans le Workshop Git & Docker ! Votre mission est de créer votre propre magasin en ligne et d'y ajouter des produits pour la grande compétition finale.

Suivez ces étapes scrupuleusement pour intégrer votre magasin au projet principal.

---

## Étape 1 : Créer le fichier de votre magasin

1. Dans votre éditeur de code, allez dans le dossier `src/website/shops/`.
2. Vous y verrez un fichier nommé `group_1.py` (le magasin de l'instructeur). 
3. **Copiez** ce fichier et renommez la copie avec votre numéro de groupe. Par exemple : `group_2.py` (si vous êtes le groupe 2).
4. Ouvrez votre nouveau fichier `group_2.py`.

## Étape 2 : Personnaliser votre magasin et vos produits

Dans votre fichier `group_2.py`, effectuez les modifications suivantes :

1. **Le nom du magasin** : Modifiez la variable `shop_name` en haut du fichier pour lui donner un nom créatif.
   ```python
   shop_name = "La Boutique Geek du Groupe 2"
   ```

2. **L'inventaire** : Ajoutez vos propres produits dans la liste `inventory`. Modifiez le nom, le prix et la catégorie. (Le stock est automatiquement initialisé à 20 pour la compétition).
   ```python
   inventory: List[Product] = [
       Product(name="Figurine Python", price=45.00, category="Décoration", image_filename="python.jpg"),
       Product(name="T-shirt Codeur", price=120.00, category="Vêtements", image_filename="tshirt.jpg"),
   ]
   ```

3. **Les images (Optionnel)** : Si vous avez précisé un `image_filename`, n'oubliez pas d'ajouter l'image correspondante dans le dossier `src/website/static/img/`.

## Étape 3 : "Brancher" votre magasin à l'application principale

Votre fichier est créé, mais l'application principale ne le connaît pas encore ! Vous devez modifier deux fichiers importants.

### Modification de `main.py` (dans `src/website/main.py`)
Ouvrez le fichier `main.py` et cherchez la section des imports (vers la ligne 9) :
```python
# Avant :
from website.shops import group_1

# APRÈS (ajoutez votre groupe) :
from website.shops import group_1, group_2
```

Cherchez la section `# Include shop routers` (vers la ligne 34) et ajoutez votre routeur :
```python
app.include_router(group_1.router, prefix="/api/1", tags=["1 Shop"])
app.include_router(group_2.router, prefix="/api/2", tags=["2 Shop"]) # <- Votre ligne
```

Cherchez la fonction `index_web` (vers la ligne 82) et ajoutez votre magasin à la liste `shops` :
```python
    shops = [
        {"id": "1", "name": group_1.shop_name},
        {"id": "2", "name": group_2.shop_name}  # <- Votre ligne
    ]
```

Cherchez les fonctions `shop_web` et `results_page` et mettez à jour le dictionnaire `shop_modules` :
```python
    # Mettre à jour dans shop_web ET dans results_page :
    shop_modules = {"1": group_1, "2": group_2} 
```

### Modification de `init_db.py` (dans `src/website/core/init_db.py`)
C'est ce fichier qui permet de sauvegarder vos produits dans la base de données.
Ouvrez-le, importez votre groupe en haut du fichier, puis ajoutez votre inventaire dans le dictionnaire `shops_data` :
```python
from website.shops import group_1, group_2  # N'oubliez pas l'import en haut !

# ... plus bas dans le fichier :
    shops_data = {
        "1": group_1.inventory,
        "2": group_2.inventory,  # <- Votre ligne
    }
```

## Étape 4 : Tester et Envoyer (Git)

1. En local, lancez la commande `uvicorn website.main:app --reload` (en vous plaçant dans le dossier `src`).
2. Allez sur `http://127.0.0.1:8000` et vérifiez que votre magasin apparaît bien sur la page d'accueil avec vos produits.
3. Si tout fonctionne, il est temps d'envoyer votre travail !
   ```bash
   git add .
   git commit -m "Ajout du magasin du groupe 2"
   git push
   ```

Bonne chance pour la compétition ! 🚀
