DROP TABLE IF EXISTS dealers;
DROP TABLE IF EXISTS cars;

CREATE TABLE dealers
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE cars
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    brand     TEXT NOT NULL,
    model     TEXT NOT NULL,
    color     TEXT NOT NULL,
    dealer_id INTEGER,
    FOREIGN KEY (dealer_id)
        REFERENCES dealers (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

