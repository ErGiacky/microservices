
use Libri;

-- Creazione della tabella "books"
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_year INTEGER NOT NULL
);
-- Inserimento di dati nella tabella "books"
INSERT INTO books (title, author, published_year) VALUES
    ('Il Signore degli Anelli', 'J.R.R. Tolkien', 1954),
    ('1984', 'George Orwell', 1949),
    ('Il Piccolo Principe', 'Antoine de Saint-Exupéry', 1943),
    ('Cime tempestose', 'Emily Brontë', 1847),
    ('Il Grande Gatsby', 'F. Scott Fitzgerald', 1925),
    ('Cronache di Narnia', 'C.S. Lewis', 1950),
    ('Guerra e Pace', 'Lev Tolstoj', 1869),
    ('Orgoglio e Pregiudizio', 'Jane Austen', 1813),
    ('Il nome della rosa', 'Umberto Eco', 1980),
    ('Il Conte di Montecristo', 'Alexandre Dumas', 1844),
    ('Anna Karenina', 'Lev Tolstoj', 1877),
    ('Don Chisciotte', 'Miguel de Cervantes', 1605),
    ('Moby Dick', 'Herman Melville', 1851),
    ('L\'Odissea', 'Omero', -800),
    ('Cent'anni di Solitudine', 'Gabriel García Márquez', 1967),
    ('Il processo', 'Franz Kafka', 1925),
    ('Il ritratto di Dorian Gray', 'Oscar Wilde', 1890),
    ('Il vecchio e il mare', 'Ernest Hemingway', 1952),
    ('Il Sermone della Montagna', 'Gesù Cristo', 30),
    ('Il Codice da Vinci', 'Dan Brown', 2003);
