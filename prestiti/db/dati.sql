Use Prestito;

CREATE TABLE IF NOT EXISTS prestiti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    libro_id INT NOT NULL,
    utente_id INT NOT NULL,
    data_prestito TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_restituzione TIMESTAMP
);

-- Inserisci 10 esempi di prestiti
INSERT INTO prestiti (libro_id, utente_id, data_prestito, data_restituzione) VALUES
  (1, 1, '2023-01-01', '2023-01-15'),
  (2, 2, '2023-02-05', '2023-02-20'),
  (3, 3, '2023-03-10', '2023-03-25'),
  (4, 4, '2023-04-15', '2023-05-01'),
  (5, 5, '2023-05-20', '2023-06-05'),
  (1, 6, '2023-06-15', '2023-07-01'),
  (2, 7, '2023-07-05', '2023-07-20'),
  (3, 8, '2023-08-10', '2023-08-25'),
  (4, 9, '2023-09-15', '2023-10-01'),
  (5, 10, '2023-10-20', '2023-11-05');
