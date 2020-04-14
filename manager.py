import json
from store import Store
from exceptions import ProductPriceException
"""
обращаем внимание на этот импорт, он на пригодится. Подробнее почитать можно по ссылке ниже.

https://python-scripts.com/json

"""

class Manager:
    """
    Менеджер это класс в котором будут находиться статические методы для работы с нашими продуктами и магазином

    @staticmethod

    """
    store = None  #это получается обьект

    @staticmethod
    def create_add_to_store_products():
        """
        Метод, который создает магазин (вызывает метод create_store для создания.)
        Спрашивает не желаете ли создать продукт. И если ответ положительный - создает продукт (create_product).
        с помощью while и какого-то условия можно повторять процесс создания продукта, до тех пор,
        пока пользователь не решит что продукты создавать больше не нужно. И не ответит на вопрос о желании
        создать продукт отрицательно.
        """

        while True:

            print('Добавить продукт в магазин?, введите Y/N.')
            user_input = input('Ваш выбор :\n').upper()
            if user_input == 'Y':
                Manager.store=Manager.create_store()
                try:
                    product=Manager.create_product()
                except ProductPriceException as err:
                    print(err)
                    print('Внимание!Пересоздайте продукт, неправильная цена>1000')
                    product = Manager.create_product()
                number=input(f'Введите количество {product.title} в магазине {Manager.store.title}:')
                print('*'*20)
                Manager.store.add_product(product,int(number))
            elif user_input == 'N':
                Manager.dump_data_to_file()
                break
               #exit('Программа завершила свою работу по причине: запрос от пользователя.')
            else:
                print('Вводить можно только Y/N')



    @staticmethod
    def create_product():
        """
        Метод который запускает процесс создания продукта, и просит ввести данные с клавиатуры.
        Возвращает продукт.
        """
        title = input('Введите название товара: ').upper()
        while True:
            price = input('Введите цену товара: ')
            if price.isnumeric() == False:
                print('Введите число')
            else:
                print('Создается продукт %s' %(title))
                return Product(title=title, price=price)
                break




    @staticmethod
    def create_store():
        """
        Метод который создает магазин и помезает его в аттрибут класса store. (Manager.store) Если магазин
        уже создан и добавлен, то метод возвращает текущий магазани, а не пересоздает новый.
        """
        if Manager.store is None:
            store_title = input('Введите название магазина:\n').upper()
            Manager.store = Store(title=store_title)
            print('Создан магазин %s'% store_title)

        return Manager.store


    @staticmethod
    def dump_data_to_file():
        """
        Метод на основе данных о нашем магазине, и товарах генеррирует JSON , который сбрасывает в файл.
        Нам может помочь json.dump()
        """

        store_data = open('store_data.txt', 'w',encoding="UTF-8")
       # with open('store_data.txt', 'w',encoding="UTF-8") as store_data:
        store_title=Manager.store.title
        data_dict = {'store_title':store_title, 'storage':[]}
        for product in Manager.store.storage:
            product_title=product.title
            product_price=product.price
            product_count=Manager.store.storage[product]
            data_dict['storage'].append((product_title,product_price,product_count))
        j=json.dump(data_dict, store_data,ensure_ascii=False)
        store_data.close()
        print(f"магазин {store_title} записан в файл 'store_data.txt'")
        print(j)


    @staticmethod
    def load_data_from_file():
        """
        Метод вычитывает JSON из файла, конвертирует его в словарь, после чего вычитывая данные
        из словаря генерирует обьекты с нужными параметрами. Так чтобы восстановить состояние магазина и товаров,
        которе было во время вызова dump_data_to_file()
        Нам может помочь json.load()
        """
        # 2sposob- with open ('store_data.txt',r,encoding="UTF-8") as store_data:
        try:
            store_data=open('store_data.txt', 'r',encoding = "utf-8")
        except FileNotFoundError:
            print('файл store_data.txt не найден')
        else:
            data=json.load(store_data)
            Manager.store=Store(title=data['store_title'])

            for record in data['storage']:
                product=Product(title=record[0],price=record[1])
                Manager.store.add_product(product=product,number_of_products=record[2])
            store_data.close()
