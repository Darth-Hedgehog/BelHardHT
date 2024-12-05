from abc import abstractmethod


class Transport:

    mileage: int = 0

    def __init__(self, brand: str, model: str, issue_year: str, color: str):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0

    @abstractmethod
    def move(self, num_km):
        try:
            if num_km > 0:

                self.mileage += num_km
        except ValueError:
            print(f"Расстояние должно быть положительным числом")


class Car(Transport):

    def __init__(self, brand: str, model: str, issue_year: str, color: str, engine_type: str):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {self.mileage} километров"


class Airplane(Transport):

    def __init__(self, brand: str, model: str, issue_year: str, color: str, lifting_capacity: int):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {self.mileage} километров"

jiguli_its_a_beer = Car('Jiguli', '5', 1967, 'Cherry', 'DVS')
broiler_ne_747 = Airplane('Kurara', 'Peven', 2023, 'vletel iz pushki v stenu', 13)

print(jiguli_its_a_beer.move(2167))
print(broiler_ne_747.move(0.013))
