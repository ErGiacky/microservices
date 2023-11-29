from flask import Flask, jsonify, request
import mysql.connector
import logging

app = Flask(__name__)

# Configura il logger
logging.basicConfig(filename='libri.log', filemode="w",level=logging.INFO)

# Configurazione della connessione al database
db_config = {
    'user': 'sa',
    'password': 'password',
    'host': 'dbprestiti',
    'database': 'Prestito'
}

# Funzione per ottenere una connessione al database
def get_db_connection():
    return mysql.connector.connect(**db_config)

logging.info("Connessione database...")

# Rotta per ottenere tutti i prestiti
@app.route('/prestiti', methods=['GET'])
def get_prestiti():
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per ottenere i prestiti
        cursor.execute("SELECT * FROM prestiti")
        prestiti_mysql = cursor.fetchall()

        # Chiudi il cursore e la connessione
        cursor.close()
        db.close()

        return jsonify({'prestiti_mysql': prestiti_mysql})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per ottenere un prestito specifico
@app.route('/prestiti/<int:prestito_id>', methods=['GET'])
def get_prestito(prestito_id):
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per ottenere un prestito specifico
        cursor.execute("SELECT * FROM prestiti WHERE id = %s", (prestito_id,))
        prestito_mysql = cursor.fetchone()

        # Chiudi il cursore e la connessione
        cursor.close()
        db.close()

        if prestito_mysql:
            return jsonify({'prestito_mysql': prestito_mysql})
        else:
            return jsonify({'message': 'Prestito non trovato'}), 404

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per aggiungere un nuovo prestito
@app.route('/prestiti', methods=['POST'])
def add_prestito():
    try:
        data = request.get_json()
        libro_id = data['libro_id']
        utente_id = data['utente_id']

        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per inserire un nuovo prestito
        cursor.execute("INSERT INTO prestiti (libro_id, utente_id) VALUES (%s, %s)", (libro_id, utente_id,))

        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Prestito aggiunto con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per aggiornare un prestito
@app.route('/prestiti/<int:prestito_id>', methods=['PUT'])
def update_prestito(prestito_id):
    try:
        data = request.get_json()
        libro_id = data['libro_id']
        utente_id = data['utente_id']

        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per aggiornare un prestito
        cursor.execute("UPDATE prestiti SET libro_id=%s, utente_id=%s WHERE id=%s", (libro_id, utente_id, prestito_id,))

        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Prestito aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per eliminare un prestito
@app.route('/prestiti/<int:prestito_id>', methods=['DELETE'])
def delete_prestito(prestito_id):
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per eliminare un prestito
        cursor.execute("DELETE FROM prestiti WHERE id=%s", (prestito_id,))

        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Prestito eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})
    
logging.warning("esecuzione prestiti/app.py...")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
