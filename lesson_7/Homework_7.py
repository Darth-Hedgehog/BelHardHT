
class Phone:

    def __init__(self, brand: str, model: str, issue_year: int):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name: str):
        self.name = name
        return f'Звонит {self.name}'

    def get_info(self):
        info = [self.brand, self.model, self.issue_year]
        return info

    def __str__(self):
        return { 'Бренд': self.brand, 'Модель': self.model, 'Год выпуска': self.issue_year}


tel = Phone('Megasonius', 'Fast-line caller', 1898)

print(tel.receive_call('+372 22 780 90 98'))
print(tel.get_info())
print(tel.__str__())
