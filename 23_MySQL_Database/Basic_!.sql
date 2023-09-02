drop tables champtb;

CREATE TABLE champtb (
    Rating INT,
    Book  VARCHAR(40),
    Price   DECIMAL(16,2),
    PRIMARY KEY(Rating, Book));
INSERT INTO champtb VALUES
    (4,"Power of Subconscious Mind",99.45),(3,"Attitude is Everything",50.99),(4,"Rich Dad Poor Dad",89.99);

SELECT * FROM champtb ORDER BY Rating;