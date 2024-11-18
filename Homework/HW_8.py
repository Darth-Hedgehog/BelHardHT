
class Transport():
    mileage: int = 0
    def __init__(self, brand: str, model: str, issue_year: str, color: str):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0


    def move(self, num_km):
        try:
            if self.num_km > 0:
                self.mileage += self.num_km
        except:
            



