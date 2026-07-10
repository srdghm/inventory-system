from models.material import Material
from inventory.db.database import get_connection


class MaterialRepository:

    def get_all(self) -> list[Material]:
        with get_connection() as connection:
            cursor= connection.cursor()
            cursor.execute("SELECT * FROM materials")
            rows = cursor.fetchall()
            materials = []

            for row in rows:
                m= Material(row[0], row[1], row[2], row[3], row[4])
                materials.append(m)
        print(materials)
        return materials

