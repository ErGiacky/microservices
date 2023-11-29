from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

#Connection string per collegarsi al db Utenti
conn = mysql.connector.connect(user='sa',
password='password',
host='dblibri',
database='Libri')

db = mysql.connector.connect(conn)
cursor = conn.cursor()

# Rotta per ottenere tutti i libri
@app.route('/libri', methods=['GET'])
def get_libri():
    try:
        # Esegui una query per ottenere i libri
        cursor.execute("SELECT * FROM libri")
        libri = cursor.fetchall()

        # Converte i risultati in un formato JSON e li restituisce
        return jsonify({'libri': libri})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per ottenere un libro specifico
@app.route('/libri/<int:libro_id>', methods=['GET'])
def get_libro(libro_id):
    try:
        # Esegui una query per ottenere un libro specifico
        cursor.execute("SELECT * FROM libri WHERE id = %s", (libro_id,))
        libro = cursor.fetchone()

        if libro:
            return jsonify({'libro': libro})
        else:
            return jsonify({'message': 'Libro non trovato'}), 404

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per aggiungere un nuovo libro
@app.route('/libri', methods=['POST'])
def add_libro():
    try:
        data = request.get_json()
        titolo = data['titolo']
        autore = data['autore']

        # Esegui una query per inserire un nuovo libro
        cursor.execute("INSERT INTO libri (titolo, autore) VALUES (%s, %s)", (titolo, autore))
        db.commit()

        return jsonify({'message': 'Libro aggiunto con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per aggiornare un libro
@app.route('/libri/<int:libro_id>', methods=['PUT'])
def update_libro(libro_id):
    try:
        data = request.get_json()
        titolo = data['titolo']
        autore = data['autore']

        # Esegui una query per aggiornare un libro
        cursor.execute("UPDATE libri SET titolo=%s, autore=%s WHERE id=%s", (titolo, autore, libro_id))
        db.commit()

        return jsonify({'message': 'Libro aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per eliminare un libro
@app.route('/libri/<int:libro_id>', methods=['DELETE'])
def delete_libro(libro_id):
    try:
        # Esegui una query per eliminare un libro
        cursor.execute("DELETE FROM libri WHERE id=%s", (libro_id,))
        db.commit()

        return jsonify({'message': 'Libro eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
