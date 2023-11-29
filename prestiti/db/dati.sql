Use Prestito;

CREATE TABLE IF NOT EXISTS prestiti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    libro_id INT NOT NULL,
    utente_id INT NOT NULL,
    data_prestito TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_restituzione TIMESTAMP
);

-- Inserisci 10 esempi di prestiti
INSERT INTO prestiti (libro_id, utente_id) VALUES
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5),
  (1, 6),
  (2, 7),
  (3, 8),
  (4, 9),
  (5, 10);
