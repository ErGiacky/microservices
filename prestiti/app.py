from flask import Flask, jsonify, request
import mysql.connector
import couchdb

app = Flask(__name__)

# Connessione al database MySQL (Prestiti)
conn_prestiti_mysql = mysql.connector.connect(
    user='sa',
    password='password',
    host='dbprestiti',
    database='Prestiti'
)
db_prestiti_mysql = mysql.connector.connect(connection=conn_prestiti_mysql)
cursor_prestiti_mysql = db_prestiti_mysql.cursor()

# Connessione al database CouchDB (Prestiti)
couch = couchdb.Server(url='http://admin:alessio@couchserver:5984/')
db_prestiti_couch = couch['prestiti']

# Rotte per i prestiti
@app.route('/prestiti', methods=['GET'])
def get_prestiti():
    try:
        # MySQL
        cursor_prestiti_mysql.execute("SELECT * FROM prestiti")
        prestiti_mysql = cursor_prestiti_mysql.fetchall()

        # CouchDB
        prestiti_couch = [db_prestiti_couch[id] for id in db_prestiti_couch]

        return jsonify({'prestiti_mysql': prestiti_mysql, 'prestiti_couch': prestiti_couch})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prestiti/<int:prestito_id>', methods=['GET'])
def get_prestito(prestito_id):
    try:
        # MySQL
        cursor_prestiti_mysql.execute("SELECT * FROM prestiti WHERE id = %s", (prestito_id,))
        prestito_mysql = cursor_prestiti_mysql.fetchone()

        # CouchDB
        prestito_couch = db_prestiti_couch[str(prestito_id)]

        return jsonify({'prestito_mysql': prestito_mysql, 'prestito_couch': prestito_couch})

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

        # CouchDB
        prestito_couch = {
            'libro_id': libro_id,
            'utente_id': utente_id
        }
        doc = db_prestiti_couch.save(prestito_couch)

        return jsonify({'message': 'Prestito aggiunto con successo', 'prestito_id': doc['_id']})

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

        # CouchDB
        prestito_couch = db_prestiti_couch[str(prestito_id)]
        prestito_couch['libro_id'] = libro_id
        prestito_couch['utente_id'] = utente_id
        db_prestiti_couch.save(prestito_couch)

        return jsonify({'message': 'Prestito aggiornato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prestiti/<int:prestito_id>', methods=['DELETE'])
def delete_prestito(prestito_id):
    try:
        # MySQL
        cursor_prestiti_mysql.execute("DELETE FROM prestiti WHERE id=%s", (prestito_id,))
        db_prestiti_mysql.commit()

        # CouchDB
        prestito_couch = db_prestiti_couch[str(prestito_id)]
        db_prestiti_couch.delete(prestito_couch)

        return jsonify({'message': 'Prestito eliminato con successo'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
