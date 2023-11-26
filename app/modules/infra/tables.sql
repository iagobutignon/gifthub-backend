CREATE DATABASE fabrico;

CREATE TABLE users (
    id UUID NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR (16) NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY (id),
    CONSTRAINT email_unique UNIQUE(email)
);

CREATE TABLE profiles (
    id UUID NOT NULL,
    user_id UUID NOT NULL,
    address_id UUID NOT NULL,
    image BLOB,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    CONSTRAINT profile_pk PRIMARY KEY (id),
    CONSTRAINT users_profiles_fk FOREIGN KEY (user_id) REFERENCES users(id)
    CONSTRAINT addresses_profiles_fk FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE events (
    id UUID NOT NULL,
    user_id UUID NOT NULL,
    address_id UUID NOT NULL,
    name VARCHAR(50) NOT NULL,
    date DATETIME NOT NULL,
    description VARCHAR(500),
    CONSTRAINT event_pk PRIMARY KEY (id),
    CONSTRAINT users_events_fk FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT addresses_events_fk FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE addresses (
    id UUID NOT NULL,
    event_id UUID,
    user_id UUID,
    number VARCHAR(10) NOT NULL,
    street VARCHAR(50) NOT NULL,
    district VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    cep VARCHAR(50) NOT NULL,
    complement VARCHAR(50) NOT NULL,
    CONSTRAINT addresses_pk PRIMARY KEY (id),
    CONSTRAINT user_addresses_fk FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT event_addresses_fk FOREIGN KEY (event_id) REFERENCES events(id)
)

CREATE TABLE products (
    id UUID NOT NULL,
    event_id UUID NOT NULL,
    image BLOB NOT NULL,
    name VARCHAR(50) NOT NULL,
    value DECIMAL(6,2) NOT NULL,
    description VARCHAR(500),
    CONSTRAINT product_pk PRIMARY KEY (id),
    CONSTRAINT product_fk FOREIGN KEY (event_id) REFERENCES events(id)
);