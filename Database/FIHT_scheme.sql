CREATE TABLE IF NOT EXISTS Food(
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR (100) NOT NULL,
    food_quantity FLOAT NOT NULL,
    food_expiration DATE,
    food_type VARCHAR (100)
);