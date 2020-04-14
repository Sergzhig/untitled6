class Product:
    def __init__(self, title, price):
        if int(price) > 1000:
            raise ProductPriceException('Завозим продукты по цене <1000')
        self.title = title
        self.price = int(price)
