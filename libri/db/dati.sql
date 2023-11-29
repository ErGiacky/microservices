
use Libri;

-- Creazione della tabella "books"
CREATE TABLE IF NOT EXISTS books (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_year INTEGER DEFAULT NULL
);
-- Inserimento di dati nella tabella "books"
INSERT INTO books (id, title, author, published_year) VALUES
    (1, 'Il Signore degli Anelli', 'J.R.R. Tolkien', 1954),
    (2, '1984', 'George Orwell', 1949),
    (3, 'Il Piccolo Principe', 'Antoine de Saint-Exupéry', 1943),
    (4, 'Cime tempestose', 'Emily Brontë', 1847),
    (5, 'Il Grande Gatsby', 'F. Scott Fitzgerald', 1925),
    (6, 'Cronache di Narnia', 'C.S. Lewis', 1950),
    (7, 'Guerra e Pace', 'Lev Tolstoj', 1869),
    (8, 'Orgoglio e Pregiudizio', 'Jane Austen', 1813),
    (9, 'Il nome della rosa', 'Umberto Eco', 1980),
    (10, 'Il Conte di Montecristo', 'Alexandre Dumas', 1844),
    (11, 'Anna Karenina', 'Lev Tolstoj', 1877),
    (12, 'Don Chisciotte', 'Miguel de Cervantes', 1605),
    (13, 'Moby Dick', 'Herman Melville', 1851),
    (14, 'Odissea', 'Omero', -800),
    (15, 'Cento anni di Solitudine', 'Gabriel García Márquez', 1967),
    (16, 'Il processo', 'Franz Kafka', 1925),
    (17, 'Il ritratto di Dorian Gray', 'Oscar Wilde', 1890),
    (18, 'Il vecchio e il mare', 'Ernest Hemingway', 1952),
    (19, 'Il Sermone della Montagna', 'Gesù Cristo', 30),
    (20, 'Il Codice da Vinci', 'Dan Brown', 2003);

