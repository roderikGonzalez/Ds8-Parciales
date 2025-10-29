import os
import psycopg2
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Obtener las variables de entorno
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

def get_connection():
    """Establece y devuelve una conexión a la base de datos PostgreSQL."""
    try:
        conn = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME,
        )
        return conn
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
