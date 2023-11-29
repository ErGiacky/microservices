Use Prestito;

CREATE TABLE IF NOT EXISTS prestiti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    libro_id INT NOT NULL,
    utente_id INT NOT NULL,
    data_prestito TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_restituzione TIMESTAMP,
    FOREIGN KEY (libro_id) REFERENCES books(id),
    FOREIGN KEY (utente_id) REFERENCES Utente(id)
);

-- Inserisci 10 esempi di prestiti
INSERT INTO prestiti (id,libro_id, utente_id) VALUES
  ('1',1, 1),
  ('2',2, 2),
  ('3',3, 3),
  ('4',4, 4),
  ('5',5, 5),
  ('6',1, 6),
  ('7',2, 7),
  ('8',3, 8),
  ('9',4, 9),
  ('10',5, 10);
