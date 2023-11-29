from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

#Connection string per collegarsi al db Utenti
conn = mysql.connector.connect(user='sa',
password='password',
host='dbutenti',
database='Utenti')

cursor = conn.cursor()

# Rotta per ottenere tutti gli utenti
@app.route('/utenti', methods=['GET'])
def get_utenti():
    try:
        # Esegui una query per ottenere gli utenti
        cursor.execute("SELECT * FROM utenti")
        utenti = cursor.fetchall()

        # Converte i risultati in un formato JSON e li restituisce
        return jsonify({'utenti': utenti})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per ottenere un utente specifico
@app.route('/utenti/<int:utente_id>', methods=['GET'])
def get_utente(utente_id):
    try:
        # Esegui una query per ottenere un utente specifico
        cursor.execute("SELECT * FROM utenti WHERE id = %s", (utente_id,))
        utente = cursor.fetchone()

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
        email = data['email']

        # Esegui una query per inserire un nuovo utente
        cursor.execute("INSERT INTO utenti (nome, cognome, email) VALUES (%s, %s, %s)", (nome, cognome, email))
        db.commit()

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
        email = data['email']

        # Esegui una query per aggiornare un utente
        cursor.execute("UPDATE utenti SET nome=%s, cognome=%s, email=%s WHERE id=%s", (nome, cognome, email, utente_id))
        db.commit()

        return jsonify({'message': 'Utente aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

# Rotta per eliminare un utente
@app.route('/utenti/<int:utente_id>', methods=['DELETE'])
def delete_utente(utente_id):
    try:
        # Esegui una query per eliminare un utente
        cursor.execute("DELETE FROM utenti WHERE id=%s", (utente_id,))
        db.commit()

        return jsonify({'message': 'Utente eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
