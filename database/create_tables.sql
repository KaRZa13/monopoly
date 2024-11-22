-- Ce fichier est là en cas de partage du projet en gros ça sert de doc technique

CREATE TABLE properties (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    cost INT,
    rent INT,
    owner_id INT NULL,
);

CREATE TABLE player (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance INT,
);