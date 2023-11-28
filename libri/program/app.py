from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)



db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

# Crea il database e il modello
with app.app_context():
    db.create_all()

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    response = [{'title': book.title, 'author': book.author, 'published_year': book.published_year, 'id': book.id} for book in books]
    return jsonify(response), 200

@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        response = {'title': book.title, 'author': book.author, 'published_year': book.published_year, 'id': book.id}
        return jsonify(response), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    published_year = data.get('published_year')

    if title and author and published_year:
        new_book = Book(
            id=str(uuid.uuid4()),
            title=title,
            author=author,
            published_year=published_year
        )

        db.session.add(new_book)
        db.session.commit()

        response = {'message': 'Book added successfully', 'id': new_book.id}
        return jsonify(response), 201
    else:
        return jsonify({'message': 'Invalid data supplied'}), 400

@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    published_year = data.get('published_year')

    if title or author or published_year:
        book = Book.query.get(book_id)

        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if published_year:
                book.published_year = published_year

            db.session.commit()

            return jsonify({'message': 'Book updated successfully'}), 200
        else:
            return jsonify({'message': 'Book not found'}), 404
    else:
        return jsonify({'message': 'No valid data supplied'}), 400

@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
