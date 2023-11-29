import requests
import json
import unittest
from flask import Flask

class TestUtentiAPI(unittest.TestCase):
    base_url = "http://127.0.0.1:5000"  # Assicurati che l'URL sia corretto

    def setUp(self):
        # Inizializza l'app Flask per il test
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_get_utenti(self):
        response = requests.get(f"{self.base_url}/utenti")
        self.assertEqual(response.status_code, 200)
        utenti = response.json()
        self.assertTrue('utenti' in utenti)

    def test_get_utente(self):
        # Supponiamo che ci sia almeno un utente nel database
        response = requests.get(f"{self.base_url}/utenti/1")
        self.assertEqual(response.status_code, 200)
        utente = response.json()
        self.assertTrue('utente' in utente)

    def test_add_utente(self):
     nuovo_utente = {
        "nome": "NuovoNome",  # Assicurati di includere il campo 'nome'
        "cognome": "NuovoCognome",
        "mail": "nuovo@utente.com"  # Assicurati di includere il campo 'mail'
    }
     response = requests.post(f"{self.base_url}/utenti", json=nuovo_utente)
     print(response.json())  # Stampa la risposta per debug
     self.assertEqual(response.status_code, 200)
     risposta = response.json()
     # Modifica l'asserzione in base alla struttura effettiva della risposta
     self.assertTrue('error' not in risposta)


    def test_update_utente(self):
        utente_da_aggiornare = {
            "nome": "baolo",
            "cognome": "lol",
            "mail": "nuovo@utente.com"
        }
        response = requests.put(f"{self.base_url}/utenti/1", json=utente_da_aggiornare)
        print(response.json())  # Stampa la risposta per debug
        self.assertEqual(response.status_code, 200)
        risposta = response.json()
        # Modifica l'asserzione in base alla struttura effettiva della risposta
        self.assertTrue('error' not in risposta)

    def test_delete_utente(self):
        # Esegui una richiesta DELETE alla tua API
        cancella_utente = {
            "nome": "",
            "cognome": "",
            "email": ""
        }
        response = requests.delete(f"{self.base_url}/utenti/7", json=cancella_utente)
        # Assicurati che la risposta sia 200
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
