class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def info(self):
        print(self.brand + " стоит " + str(self.price))

phone = Phone("Samsung", 50000)
phone.info()