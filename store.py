from product import Product

class Store:
    def __init__(self, title="Магазин на диване"):
        self.title = title

        """
        1. self.storage = { "banana": 3 } - возможно хранить информацию о количестве, 
        и ключем будет строка (название продукту)
        
        2. self.storage = { object: 12 } - возможно хранить информацию о количестве, 
        и ключем будет сам объект.
        
        3.  self.storage = [ object, object2, object3 ]  - возможно хранить список объектов (товаров),
        и количество придется каждый раз высчитывать при необходимости 
        """

        self.storage = {}

    def add_product(self, product, number_of_products=1):
        """
        так как я храню данные как указано в пункте 2 выше, то моя реализация добавления продукта выглядит так
        """
        if product in self.storage:
            self.storage[product] += int(number_of_products)
        else:
            self.storage[product] = int(number_of_products)

    def _product_details(self, product):
        message_template = "Количество товара %s: %s штук, стоимость: %s. Суммарная стоимость: %s "

        product_count = self.storage[product]
        product_title = product.title
        product_price = product.price
        product_total_price = product_price * product_count

        rendered_message = message_template % (product_title, product_count, product_price, product_total_price)

        return rendered_message

    def showcase(self, product=None):
        print(f"Отчет по магазину {self.title}:")
        if product:
            print(self._product_details(product))
        else:
            for product in self.storage.keys():
                print(self._product_details(product))




#if __name__=='__main__':



