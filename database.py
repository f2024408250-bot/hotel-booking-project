import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", 5432)
    )
    return conn


def save_booking(full_name, email, phone, check_in, check_out, room_type, guests, special_requests):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings (full_name, email, phone, check_in, check_out, room_type, guests, special_requests)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (full_name, email, phone, check_in, check_out, room_type, guests, special_requests))

    conn.commit()
    cursor.close()
    conn.close()
