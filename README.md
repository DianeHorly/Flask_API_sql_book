                                                        Rapport d'utilisation de l'application Flask
                              1. Introduction
Ce document décrit le fonctionnement d'une application web construite à l'aide de Flask, un microframework Python. L'application gère une collection de livres stockés dans une base de données SQLite,
permettant aux utilisateurs de récupérer, ajouter, mettre à jour et supprimer des livres via des requêtes HTTP.

                              2. Structure du Code
Le code est organisé comme suit :

Flask Application: L'application est définie à l'aide du module Flask.
Base de Données: Une base de données SQLite est utilisée pour stocker les informations sur les livres, et est gérée par le module dataset.
Routes HTTP: Des routes spécifiques sont définies pour manipuler la collection de livres.
                              
                              3. Fonctionnalités
L'application offre les fonctionnalités suivantes :

                          3.1 Initialisation de la Base de Données
La fonction initialize_books() est appelée au démarrage de l'application pour peupler la base de données avec une collection initiale de livres. Cette fonction :

Supprime tous les enregistrements existants pour éviter les doublons.
Insère une liste prédéfinie de livres.
3.2 Récupération des Livres
Deux fonctions sont utilisées pour récupérer les données des livres :

fetch_db(book_id) : Retourne les informations d'un livre spécifique à partir de son book_id.
fetch_db_all() : Retourne la liste complète des livres présents dans la base de données.
                          
                          3.3 Routes HTTP
L'application expose deux routes principales pour interagir avec les livres.

                          3.3.1 Route /book/books
GET: Retourne la liste complète des livres sous format JSON.
POST: Ajoute un nouveau livre. Si le livre avec l'ID spécifié existe déjà, une erreur est renvoyée.
3.3.2 Route /book/books/<book_id>
GET: Retourne les détails d'un livre spécifique identifié par book_id.
PUT: Met à jour les informations d'un livre existant. Les données doivent être envoyées au format JSON.
DELETE: Supprime un livre spécifique. Si le livre n'est pas trouvé, une erreur est renvoyée.

                              4. Détails Techniques
Pour la realisation de ce projet, j'utilise Vscode.
                        4.1 Base de Données
Type: SQLite
Table: books
Champs:
book_id : Identifiant unique du livre (chaîne de caractères)
nom : Nom du livre (chaîne de caractères)
auteur : Auteur du livre (chaîne de caractères)
                      
                       4.2 Gestion des Requêtes
Chaque route est configurée pour répondre à des méthodes HTTP spécifiques (GET, POST, PUT, DELETE). Les réponses sont formatées en JSON pour faciliter l'interaction avec les clients web.

                              5. Lancement de l'Application
Pour démarrer l'application :

--> Installez python
--> Installez les dépendances nécessaires avec pip install flask dataset.
--> Exécutez l'application avec la commande python book.py.
--> L'application tournera alors sur le port 5001 en mode débogage.
--> suivre le lien qui s'affiche, puis cliquez dessus
--> suivre les routes dans la barre de navigation du navigateur pour la vérification.
