import logging
import json
from flask import Flask, request
from flask import jsonify
import mysql.connector


app = Flask(__name__)

#Connection string per collegarsi al db Utenti
conn = mysql.connector.connect(user='sa',
password='password',
host='dbutenti',
database='Utenti')

cursor = conn.cursor()

# Route per eseguire la funzione che ritorna tutti gli utenti
@app.route('/get', methods=['GET'])
def execute_query():
    '''get'''

    cursor.execute('SELECT * FROM Utente')
    results = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in results]

    # Restituisci i risultati come JSON
    return jsonify(data)


@app.route('/get/<int:idutenteget>', methods=['GET'])
def get_data_by_id(idutenteget):
    '''getid'''
    # Esegui una query per recuperare i dati con l'ID specificato
    cursor.execute('SELECT * FROM Utente WHERE id = %s', (idutenteget,))
    result = cursor.fetchone()
    if result is None:
        return json.dumps({'error': 'Dati non trovati.'}), 404

    column_names = [desc[0] for desc in cursor.description]
    data = dict(zip(column_names, result))
    # Restituisci il risultato come JSON
    return jsonify(data)

#Crea un Utente
@app.route('/crea', methods=['POST'])
def insert_data():
    '''create'''
    data = request.get_json()

    idpost = data.get('ID')
    nome = data.get('Nome')
    cognome = data.get('Cognome')
    mail = data.get('Mail')
    telefono = data.get('Telefono')
    if idpost in cursor.fetchall():
        return json.dumps ({'error': 'ID già presente nel db.'}), 404

    #inserire errore se stesso ID
    cursor.execute(f'''INSERT INTO Utente
    (ID, Nome, Cognome, Mail, Telefono)
    VALUES ('{idpost}','{nome}' , '{cognome}', '{mail}', '{telefono}')''' )

    conn.commit()


    return 'Inserito utente nel db'

@app.route('/update/<int:idupdate>', methods=['PUT'])
def update_data(idupdate):
    '''update'''
    data = request.get_json()

    nome = data.get('Nome')
    cognome = data.get('Cognome')
    mail = data.get('Mail')
    telefono = data.get('Telefono')


    # Esegui la query di aggiornamento
    cursor.execute(f"""UPDATE Utente SET Nome
    = '{nome}', Cognome = '{cognome}', Mail = '{mail}', Telefono = '{telefono}' 
    WHERE ID = '{idupdate}'""")

    conn.commit()


    return 'Aggiornato con successo'


@app.route('/delete/<int:iddelete>', methods=['DELETE'])
def delete_data(iddelete):
    '''delete'''
    # Esegui la query di eliminazione
    cursor.execute(f"DELETE FROM Utente WHERE ID = '{iddelete}'")

    conn.commit()


    return 'Rimosso con successo'

#run dell'applicazione
if __name__ == '__main__':
    app.run(host="0.0.0.0")

logging.warning("Run dell'applicazione Utenti")
# End-of-file (EOF)