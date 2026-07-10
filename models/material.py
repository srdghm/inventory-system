class Material:

    def __init__(
        self,
        id: int | None,
        name: str,
        unit: str,
        rate: float,
        quantity: float,
    ):
        self.id = id
        self.name = name
        self.unit = unit
        self.rate = rate
        self.quantity = quantity


    def total_value(self) -> float:
        return self.rate * self.quantity


    def __repr__(self):
        return (
            f"Material("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"unit='{self.unit}', "
            f"rate={self.rate}, "
            f"quantity={self.quantity})"
        )