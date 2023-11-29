import requests
import json
import unittest
from flask import Flask

class TestPrestitiAPI(unittest.TestCase):
    base_url = "http://127.0.0.1:4998"  # Assicurati che l'URL sia corretto

    def setUp(self):
        # Inizializza l'app Flask per il test
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_get_prestiti(self):
      response = requests.get('http://127.0.0.1:4998/prestiti',timeout=30)
      print(response.json())  # JSON format 
      self.assertEqual(response.status_code, 200)
      data = response.json()    
      self.assertTrue('prestiti_mysql' in data)

    def test_get_prestito(self):
      response = requests.get('http://127.0.0.1:4998/prestiti/4',timeout=30)
      print(response.json())  # JSON format 
      self.assertEqual(response.status_code, 200)
      data = response.json()    
      self.assertTrue('prestito_mysql' in data)

    def test_add_prestito(self):
        nuovo_prestito = {
            "utente_id": 1,
            "libro_id": 1,
            "data_prestito": "2023-01-01",
            "data_scadenza": "2023-01-15"
        }
        response = requests.post(f"{self.base_url}/prestiti", json=nuovo_prestito)
        self.assertEqual(response.status_code, 200)
        risposta = response.json()
        self.assertTrue('message' in risposta)

    def test_update_prestito(self):
        prestito_da_aggiornare = {
            "utente_id": 1,
            "libro_id": 1,
            "data_prestito": "2023-01-01",
            "data_scadenza": "2023-01-20"
        }
        response = requests.put(f"{self.base_url}/prestiti/1", json=prestito_da_aggiornare)
        self.assertEqual(response.status_code, 200)
        risposta = response.json()
        self.assertTrue('message' in risposta)

    def test_delete_prestito(self):
        # Esegui una richiesta DELETE alla tua API
        response = requests.delete(f"{self.base_url}/prestiti/1")
        # Assicurati che la risposta sia 200
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
