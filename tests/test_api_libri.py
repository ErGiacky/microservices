import requests
import json
import unittest
from flask import Flask

class TestLibriAPI(unittest.TestCase):
    base_url = "http://127.0.0.1:4999"  # Assicurati che l'URL sia corretto

    def setUp(self):
        # Inizializza l'app Flask per il test
        self.app = Flask(__name__) 
        self.app.config['TESTING'] = True

    def test_get_libri(self):
        response = requests.get(f"{self.base_url}/libri")
        self.assertEqual(response.status_code, 200)
        libri = response.json()
        self.assertTrue('libri' in libri)

    def test_get_libro(self):
        # Supponiamo che ci sia almeno un libro nel database
        response = requests.get(f"{self.base_url}/libri/1")
        self.assertEqual(response.status_code, 200)
        libro = response.json()
        self.assertTrue('libro' in libro)

    def test_add_libro(self):
        nuovo_libro = {
            "titolo": "Nuovo Libro",
            "autore": "Autore Sconosciuto"
        }
        response = requests.post(f"{self.base_url}/libri", json=nuovo_libro)
        self.assertEqual(response.status_code, 200)
        risposta = response.json()
        self.assertTrue('message' in risposta)

    def test_update_libro(self):
        libro_da_aggiornare = {
            "titolo": "Nuovo cavallo pazzo",
            "autore": "Nuovo Autore"
        }
        response = requests.put(f"{self.base_url}/libri/1", json=libro_da_aggiornare)
        self.assertEqual(response.status_code, 200)
        risposta = response.json()
        self.assertTrue('message' in risposta)

    def test_delete_libro(self):
    # Esegui una richiesta DELETE alla tua API
        cancella_libro = {
            "titolo": "",
            "autore": ""
        }
        response = requests.delete(f"{self.base_url}/libri/3", json=cancella_libro)
    # Assicurati che la risposta sia 200
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
