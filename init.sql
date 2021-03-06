DROP DATABASE IF EXISTS testdb;

CREATE DATABASE IF NOT EXISTS testdb DEFAULT CHARSET=utf8;

CREATE TABLE testdb.persona (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    biografia VARCHAR(255) NULL,
    PRIMARY KEY (id)
) ENGINE = INNODB;