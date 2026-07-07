-- Create Database
CREATE DATABASE IF NOT EXISTS library_management;

USE library_management;

-- Table: Books
CREATE TABLE books (
    bname VARCHAR(100) NOT NULL,
    bcode INT PRIMARY KEY,
    total INT NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- Table: Issued Books
CREATE TABLE issuedbooks (
    name VARCHAR(100) NOT NULL,
    regno VARCHAR(20) NOT NULL,
    bcode INT NOT NULL,
    issued DATE NOT NULL,
    FOREIGN KEY (bcode) REFERENCES books(bcode)
);

-- Table: Submitted Books
CREATE TABLE submission (
    name VARCHAR(100) NOT NULL,
    regno VARCHAR(20) NOT NULL,
    bcode INT NOT NULL,
    submission DATE NOT NULL,
    FOREIGN KEY (bcode) REFERENCES books(bcode)
);