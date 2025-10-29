from src.config import get_connection

def execute_query(query, params=None, fetch=False):
    """Ejecuta una consulta SQL en la base de datos."""
    conn = get_connection()
    if not conn:
        return None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                return results
            else:
                conn.commit()
                return cursor.rowcount
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    finally:
        conn.close()

