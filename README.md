Progetto Microservizi(Biblioteca)

- Creazione di API basate su Flask comunicando con database MySQL per gestire informazioni relativamente ai tre servizi:
  Libri,Utenti e Prestiti.
- I microservizi sono orchestrati utilizzando Docker e Docker Compose.
- Sono stati implementati test utilizzando la libreria(unittest) per garantire il corretto funzionamento delle API.
- Struttura delle Tabelle:
    Utenti: Contiene informazioni sugli utenti.
    Libri: Contiene informazioni sui libri.
    Prestiti: Contiene informazioni sui prestiti, inclusi le date di prestito e restituzione.
- Un Dockerfile per ogni servizio Flask e uno docker-compose.yaml che definisce i servizi e le relative configurazioni.
- CI/CD ad ogni push di repository su GitHub si aggiorna l'immagine su DockerHub.
- Usando la libreria logging di python per tenere traccia dei file di log del vari servizi (non capisco se funzioni o meno).
- Desing pattern: service mesh(credo)



  
![diagramma_scuro](https://github.com/ErGiacky/microservices/assets/74863681/787c4c95-9554-4a7e-8dbc-831fe36e7a6f)
