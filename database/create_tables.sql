-- Ce fichier est là en cas de partage du projet en gros ça sert de doc technique
CREATE DATABASE monopoly;
USE monopoly;


CREATE TABLE player (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    balance INT DEFAULT 1500,
    position INT DEFAULT 0,
    is_in_jail BOOLEAN DEFAULT FALSE,
    turns_in_jail INT DEFAULT 0
);

CREATE TABLE board (
    id INT PRIMARY KEY AUTO_INCREMENT
    name VARCHAR(10) NOT NULL,
    type ENUM ('property', 'chance', 'community_chest', 'go', 'go_to_jail', 'tax', 'free_parking') NOT NULL,
    
);

CREATE TABLE neighborhood (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25)
    price INT
);

CREATE TABLE properties (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    cost INT,
    rent INT,
    owner_id INT NULL,
);

INSERT INTO neighborhood VALUE
(1,'Marron',50),
(2,'Noir (gare)',0),
(3,'Bleu clair',50),
(4,'Violet',100),
(5,'Blanc (Compagnies Eau et Electricité)',0),
(6,'Orange',100),
(7,'Rouge',150),
(8,'Jaune',150),
(9,'Vert',200),
(10,'Bleu foncé',200);

INSERT INTO properties VALUE    (1, 'Boulevard de Belleville')