from flask import Flask, request, jsonify, make_response
import dataset

# Création de l'application Flask
app = Flask(__name__)

# Connexion à la base de données SQLite
db = dataset.connect('sqlite:///book.db')
table = db['books']

# Fonction pour initialiser les livres dans la base de données sans doublons
def initialize_books():
    # Liste des livres initiaux
    initial_books = [
        {
            "book_id": "1",
            "nom": "A Game of Thrones",
            "auteur": "George R. R Martin"
        },
        {
            "book_id": "2",
            "nom": "Lord of the Rings",
            "auteur": "J. R. R. Tolkien"
        },
        {
            "book_id": "3",
            "nom": "Dead Man",
            "auteur": "Jim Jarmush"
        },
        {
            "book_id": "4",
            "nom": "Melancholia",
            "auteur": "Lars von Trier"
        }
    ]
    
    # Supprime tous les enregistrements existants pour éviter les doublons lors de l'initialisation
    table.delete()
    
    # Insère les livres initiaux
    for book in initial_books:
        table.insert(book)

# Initialiser la base de données avec les livres initiaux
initialize_books()

# Fonction pour récupérer un livre spécifique à partir de la base de données
def fetch_db(book_id):
    return table.find_one(book_id=book_id)

# Fonction pour récupérer tous les livres à partir de la base de données
def fetch_db_all():
    return [dict(row) for row in table.all()]

# Route pour gérer les opérations GET et POST sur la collection de livres
@app.route('/book/books', methods=['GET', 'POST'])
def app_books():
    if request.method == "GET":
        # Retourne tous les livres
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == "POST":
        # Ajoute un nouveau livre si l'ID n'existe pas déjà
        content = request.json
        book_id = content['book_id']
        if table.find_one(book_id):
            return make_response(jsonify({"error": "Book already exists"}), 400)
        table.insert(content)
        return make_response(jsonify(content), 201)

# Route pour gérer les opérations GET, PUT et DELETE sur un livre spécifique
@app.route('/book/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def app_eachBooks(book_id):
    if request.method == "GET":
        # Retourne un livre spécifique
        book_obj = fetch_db(book_id)
        if book_obj:
            return make_response(jsonify(book_obj), 200)
        else:
            return make_response(jsonify({"error": "Book not found"}), 404)
    elif request.method == "PUT":
        # Met à jour les informations d'un livre spécifique
        content = request.json
        table.update(content, ['book_id'])
        book_obj = fetch_db(book_id)
        return make_response(jsonify(book_obj), 200)
    elif request.method == "DELETE":
        # Supprime un livre spécifique
        book_obj = fetch_db(book_id)
        if book_obj:
            table.delete(book_id=book_id)
            return make_response(jsonify(book_obj), 204)
        else:
            return make_response(jsonify({"error": "Book not found"}), 404)

# Lancement de l'application Flask
if __name__ == "__main__":
    app.run(debug=True, port=5001)
