CREATE TABLE perishables(
    perish_ID SERIAL PRIMARY KEY,
    perish_name VARCHAR(100) NOT NULL,
    perish_quantity FLOAT NOT NULL,
    date_bought DATE,
    expiration_date DATE,
    shelf_life_days INTEGER
);

CREATE TABLE spices(
    spice_ID SERIAL PRIMARY KEY,
    spice_name VARCHAR(100) NOT NULL,
    spice_quantity FLOAT -- in number of bottles/jars
);

CREATE TABLE cans(
    can_ID SERIAL PRIMARY KEY,
    can_name VARCHAR(100) NOT NULL,
    can_quantity INTEGER NOT NULL,
    date_bought DATE,
    shelf_life_days INTEGER
);

CREATE TABLE boxs(
    box_ID SERIAL PRIMARY KEY,
    box_name VARCHAR(100) NOT NULL,
    box_quantity INTEGER NOT NULL
);
