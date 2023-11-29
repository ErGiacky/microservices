from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configurazione della connessione al database
db_config = {
    'user': 'sa',
    'password': 'password',
    'host': 'dbutenti',
    'database': 'Utenti'
}

# Funzione per ottenere una connessione al database
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rotta per ottenere tutti gli utenti
@app.route('/utenti', methods=['GET'])
def get_utenti():
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per ottenere gli utenti
        cursor.execute("SELECT * FROM Utente")
        utenti = cursor.fetchall()

        # Chiudi il cursore e la connessione
        cursor.close()
        db.close()

        # Converte i risultati in un formato JSON e li restituisce
        return jsonify({'utenti': utenti})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per ottenere un utente specifico
@app.route('/utenti/<int:utente_id>', methods=['GET'])
def get_utente(utente_id):
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per ottenere un utente specifico
        cursor.execute("SELECT * FROM Utente WHERE id = %s", (utente_id,))
        utente = cursor.fetchone()

        # Chiudi il cursore e la connessione
        cursor.close()
        db.close()

        if utente:
            return jsonify({'utente': utente})
        else:
            return jsonify({'message': 'Utente non trovato'}), 404

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per aggiungere un nuovo utente
@app.route('/utenti', methods=['POST'])
def add_utente():
    try:
        data = request.get_json()
        nome = data['nome']
        cognome = data['cognome']

        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per inserire un nuovo utente
        cursor.execute("INSERT INTO Utente (nome, cognome) VALUES (%s, %s)", (nome, cognome))
        
        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Utente aggiunto con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per aggiornare un utente
@app.route('/utenti/<int:utente_id>', methods=['PUT'])
def update_utente(utente_id):
    try:
        data = request.get_json()
        nome = data['nome']
        cognome = data['cognome']

        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per aggiornare un utente
        cursor.execute("UPDATE Utente SET nome=%s, cognome=%s WHERE id=%s", (nome, cognome, utente_id))
        
        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Utente aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per eliminare un utente
@app.route('/utenti/<int:utente_id>', methods=['DELETE'])
def delete_utente(utente_id):
    try:
        # Ottieni una connessione al database
        db = get_db_connection()

        # Crea un cursore per eseguire le query
        cursor = db.cursor()

        # Esegui una query per eliminare un utente
        cursor.execute("DELETE FROM Utente WHERE id=%s", (utente_id,))
        
        # Commit delle modifiche e chiusura della connessione
        db.commit()
        cursor.close()
        db.close()

        return jsonify({'message': 'Utente eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
