CREATE DATABASE book_recommender;
USE book_recommender;

CREATE TABLE book_details (
    ISBN VARCHAR(20) PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(150) NOT NULL,
    Publication_Year INT,
    Average_Rating DECIMAL(3,2),
    Image_url VARCHAR(500)
);

SHOW TABLES;
ALTER TABLE book_details
MODIFY COLUMN Average_Rating DECIMAL(4,2);

ALTER TABLE book_details
MODIFY Title TEXT;

SELECT * FROM book_details;