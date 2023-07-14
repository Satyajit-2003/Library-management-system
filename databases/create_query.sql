-- SQLite
CREATE TABLE USER (
    username varchar(20) PRIMARY KEY,
    first_name varchar(15),
    last_name varchar(15),
    email varchar(30),
    password INTEGER,
    address varchar(40),
    city varchar(20),
    state varchar(20),
    pincode INTEGER,
    phone INTEGER
);

CREATE TABLE BOOK (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    author VARCHAR(50),
    language VARCHAR(10),
    pages INTEGER,
    quantity INTEGER
);

CREATE TABLE BORROW (
    username varchar(20) REFERENCES USER(username),
    id INTEGER REFERENCES BOOK(id),
    borrowdate VARCHAR(10),
    returndate VARCHAR(10)
);

CREATE TABLE REQUEST_BOOK (
    username INTEGER REFERENCES USER(username),
    title VARCHAR(100),
    author VARCHAR(50),
    language VARCHAR(10),
    accept_date VARCHAR(10),
    PRIMARY KEY (username, title)
);
