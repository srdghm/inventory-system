from inventory.db.database import get_connection


with get_connection() as conn:
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO materials(name, unit, rate, quantity)
        VALUES (?, ?, ?, ?)
    """, ("Cement", "bag", 900, 100))