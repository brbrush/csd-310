use whatabook;

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
 ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
 ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('Minas Tirith, 123 Gondor Way');

/*
    insert book records 
*/
INSERT INTO book(book_id, book_name, author, details)
    VALUES(3, 'The Return of the King', 'Tolkien', 'being the third part of The Lord of the Rings');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(1, 'The Fellowship of the Ring', 'Tolkien', 'being the first part of The Lord of the Rings');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(2, 'The Two Towers', 'Tolkien', 'being the second part of The Lord of The Rings');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(4, 'The Adventures of Tom Bombadil', 'Tolkien', 'and Other Verses from the Red Book');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(5, 'The Silmarillion', 'Tolkien', 'Collected tales of the beginnings of Middle-Earth');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(6, 'Unfinished Tales of Numenor and Middle-Earth', 'Tolkien', 'More tales of the First, Second, and Third Ages of Middle-Earth');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(7, 'The Book of Lost Tales, Part 1', 'Tolkien', 'The History of Middle-Earth: Vol. 1');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(8, 'The Book of Lost Tales, Part 2', 'Tolkien', 'The History of Middle-Earth: Vol. 2');

INSERT INTO book(book_id, book_name, author, details)
    VALUES(9, 'The Hobbit', 'Tolkien', 'There and Back Again');

/*
    insert user
*/ 
INSERT INTO user(user_id, first_name, last_name) 
    VALUES(1, 'Aragorn', 'Elessar');

INSERT INTO user(user_id, first_name, last_name)
    VALUES(2, 'Legolas', 'from the Woodland Realm');

INSERT INTO user(user_id, first_name, last_name)
    VALUES(3, 'Gimli', 'Son of Gloin');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE user_id = 1), 
        (SELECT book_id FROM book WHERE book_id = 1)
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE user_id = 2),
        (SELECT book_id FROM book WHERE book_id = 2)
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE user_id = 3),
        (SELECT book_id FROM book WHERE book_id = 3)
    );