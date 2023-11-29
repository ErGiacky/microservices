from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Connessione al database MySQL (Prestiti)
conn_prestiti_mysql = mysql.connector.connect(
    user='sa',
    password='password',
    host='dbprestiti',
    database='Prestito'
)
db_prestiti_mysql = mysql.connector.connect(connection=conn_prestiti_mysql)
cursor_prestiti_mysql = db_prestiti_mysql.cursor()

# Rotte per i prestiti
@app.route('/prestiti', methods=['GET'])
def get_prestiti():
    try:
        # MySQL
        cursor_prestiti_mysql.execute("SELECT * FROM prestiti")
        prestiti_mysql = cursor_prestiti_mysql.fetchall()

        return jsonify({'prestiti_mysql': prestiti_mysql})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prestiti/<int:prestito_id>', methods=['GET'])
def get_prestito(prestito_id):
    try:
        # MySQL
        cursor_prestiti_mysql.execute("SELECT * FROM prestiti WHERE id = %s", (prestito_id,))
        prestito_mysql = cursor_prestiti_mysql.fetchone()

        return jsonify({'prestito_mysql': prestito_mysql})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prestiti', methods=['POST'])
def add_prestito():
    try:
        data = request.get_json()
        libro_id = data['libro_id']
        utente_id = data['utente_id']

        # MySQL
        cursor_prestiti_mysql.execute("INSERT INTO prestiti (libro_id, utente_id) VALUES (%s, %s)", (libro_id, utente_id,))
        db_prestiti_mysql.commit()

        return jsonify({'message': 'Prestito aggiunto con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prestiti/<int:prestito_id>', methods=['PUT'])
def update_prestito(prestito_id):
    try:
        data = request.get_json()
        libro_id = data['libro_id']
        utente_id = data['utente_id']

        # MySQL
        cursor_prestiti_mysql.execute("UPDATE prestiti SET libro_id=%s, utente_id=%s WHERE id=%s", (libro_id, utente_id, prestito_id))
        db_prestiti_mysql.commit()

        return jsonify({'message': 'Prestito aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prestiti/<int:prestito_id>', methods=['DELETE'])
def delete_prestito(prestito_id):
    try:
        # MySQL
        cursor_prestiti_mysql.execute("DELETE FROM prestiti WHERE id=%s", (prestito_id,))
        db_prestiti_mysql.commit()

        return jsonify({'message': 'Prestito eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
