from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

# Configurazione per la connessione a MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/booksdb'
mongo = PyMongo(app)

# Rotte

# Aggiungi un nuovo libro
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    published_year = data.get('published_year')

    if title and author and published_year:
        book_id = mongo.db.books.insert({
            'title': title,
            'author': author,
            'published_year': published_year
        })
        response = {'message': 'Book added successfully', 'id': str(book_id)}
        return jsonify(response), 201
    else:
        return jsonify({'message': 'Invalid data supplied'}), 400

# Ottieni tutti i libri
@app.route('/books', methods=['GET'])
def get_all_books():
    books = mongo.db.books.find()
    response = [{'title': book['title'], 'author': book['author'], 'published_year': book['published_year'], 'id': str(book['_id'])} for book in books]
    return jsonify(response), 200

# Ottieni un libro specifico
@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    if book:
        response = {'title': book['title'], 'author': book['author'], 'published_year': book['published_year'], 'id': str(book['_id'])}
        return jsonify(response), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Aggiorna un libro
@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    published_year = data.get('published_year')

    if title or author or published_year:
        update_data = {}
        if title:
            update_data['title'] = title
        if author:
            update_data['author'] = author
        if published_year:
            update_data['published_year'] = published_year

        result = mongo.db.books.update_one({'_id': ObjectId(book_id)}, {'$set': update_data})

        if result.modified_count > 0:
            return jsonify({'message': 'Book updated successfully'}), 200
        else:
            return jsonify({'message': 'No changes made'}), 200
    else:
        return jsonify({'message': 'No valid data supplied'}), 400

# Elimina un libro
@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = mongo.db.books.delete_one({'_id': ObjectId(book_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
