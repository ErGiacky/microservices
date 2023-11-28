use Utenti;

CREATE TABLE IF NOT EXISTS Utente (
    ID VARCHAR(36) PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Cognome VARCHAR(50) NOT NULL,
    Mail VARCHAR(120) UNIQUE NOT NULL,
    Telefono VARCHAR(20)
);

INSERT INTO Utente (ID, Nome, Cognome, Mail, Telefono) VALUES
    ('1', 'Mario', 'Rossi', 'mario.rossi@email.com', '1234567890'),
    ('2', 'Luca', 'Bianchi', 'luca.bianchi@email.com', '0987654321'),
    ('3', 'Anna', 'Verdi', 'anna.verdi@email.com', NULL),
    ('4', 'Paola', 'Neri', 'paola.neri@email.com', '1112233444'),
    ('5', 'Giovanni', 'Gialli', 'giovanni.gialli@email.com', '5556667777'),
    ('6', 'Alessia', 'Rosa', 'alessia.rosa@email.com', NULL),
    ('7', 'Marco', 'Blu', 'marco.blu@email.com', '9998887777'),
    ('8', 'Francesca', 'Viola', 'francesca.viola@email.com', '3332221111'),
    ('9', 'Roberto', 'Arancio', 'roberto.arancio@email.com', NULL),
    ('10', 'Elena', 'Celeste', 'elena.celeste@email.com', '7778889999'),
    ('11', 'Simone', 'Marrone', 'simone.marrone@email.com', '1112223333'),
    ('12', 'Valentina', 'Rossa', 'valentina.rossa@email.com', NULL),
    ('13', 'Riccardo', 'Giallo', 'riccardo.giallo@email.com', '4445556666'),
    ('14', 'Giulia', 'Blu', 'giulia.blu@email.com', '2223334444'),
    ('15', 'Davide', 'Verde', 'davide.verde@email.com', '6667778888'),
    ('16', 'Sara', 'Nera', 'sara.nera@email.com', NULL),
    ('17', 'Matteo', 'Arancio', 'matteo.arancio@email.com', '8889990000'),
    ('18', 'Laura', 'Bianca', 'laura.bianca@email.com', '1110009999'),
    ('19', 'Andrea', 'Viola', 'andrea.viola@email.com', NULL),
    ('20', 'Cristina', 'Rossa', 'cristina.rossa@email.com', '1230004567');
