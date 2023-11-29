from flask import Flask, jsonify, request
import logging
import mysql.connector

app = Flask(__name__)

# Configura il logger
logging.basicConfig(filename='libri.log', filemode="w",level=logging.INFO)

# Configurazione della connessione al database
db_config = {
    'user': 'sa',
    'password': 'password',
    'host': 'dblibri',
    'database': 'Libri'
}

# Funzione per ottenere una connessione al database
def get_db_connection():
    return mysql.connector.connect(**db_config)

logging.info("Connessione database...")

# Rotta per ottenere tutti i libri
@app.route('/libri', methods=['GET'])
def get_libri():
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per ottenere i libri
        cursor.execute("SELECT * FROM books")
        libri = cursor.fetchall()

        # Chiudi il cursore e la connessione
        cursor.close()
        db.close()


        # Converte i risultati in un formato JSON e li restituisce
        return jsonify({'libri': libri})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per ottenere un libro specifico
@app.route('/libri/<int:id>', methods=['GET'])
def get_libro(id):
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per ottenere un libro specifico
        cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
        libro = cursor.fetchone()

        # Chiudi il cursore e la connessione
        cursor.close()
        db.close()

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

        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per inserire un nuovo libro
        cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (titolo, autore,))

        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Libro aggiunto con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})


# Rotta per aggiornare un libro
@app.route('/libri/<int:id>', methods=['PUT'])
def update_libro(id):
    try:
        data = request.get_json()
        titolo = data['titolo']
        autore = data['autore']

        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per aggiornare un libro
        cursor.execute("UPDATE books SET title=%s, author=%s WHERE id=%s", (titolo, autore, id,))
        
        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({'message': 'Libro aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per eliminare un libro
@app.route('/libri/<int:id>', methods=['DELETE'])
def delete_libro(id):
    try:
        data = request.get_json()
        titolo = data['titolo']
        autore = data['autore']
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per eliminare un libro
        cursor.execute("DELETE FROM books WHERE id=%s", (id,))
        
        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Libro eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

logging.warning("esecuzione libri/app.py...")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
