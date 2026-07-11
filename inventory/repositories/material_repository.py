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
        return materials
    def add(self, material: Material) -> None:

        with get_connection() as connection:
             cursor = connection.cursor()
             cursor.execute(
                 "INSERT INTO materials (name, unit, rate, quantity) VALUES (?, ?, ?, ?)",
                    (
                    material.name,
                    material.unit,
                    material.rate,
                    material.quantity,
                    ),
                )
        material.id = cursor.lastrowid

