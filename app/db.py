import psycopg2

import os


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Sprawdzamy, czy tabela istnieje
    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id SERIAL PRIMARY KEY,
        city VARCHAR(100),
        temp REAL,
        description VARCHAR(255)
    );
    """)
    conn.commit()
    cur.close()
    conn.close()


def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "weatherdb"),
        user=os.getenv("DB_USER", "weatheruser"),
        password=os.getenv("DB_PASSWORD", "weatherpass")
    )


# Funkcja do zapisywania pogody w bazie
def save_weather(city, temp, description):
    conn = get_conn()
    cur = conn.cursor()

    # Dodajemy dane do tabeli
    cur.execute("""
    INSERT INTO weather (city, temp, description)
    VALUES (%s, %s, %s);
    """, (city, temp, description))

    conn.commit()
    cur.close()
    conn.close()


# Funkcja do pobierania danych o pogodzie
def get_all_weather():
    conn = get_conn()
    cur = conn.cursor()

    # Pobieramy ostatnie 10 rekordów z tabeli
    cur.execute("""
    SELECT city, temp, description FROM weather ORDER BY id DESC LIMIT 10;
    """)

    # Zbieramy dane
    weather_data = cur.fetchall()

    cur.close()
    conn.close()

    return weather_data


# Inicjalizacja bazy danych przy starcie
init_db()
