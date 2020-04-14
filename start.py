from manager import Manager



print('Создаем магазин c продуктами')
Manager.create_store()
print('Добавляем товары в магазин и записываем в файл:')
Manager.create_add_to_store_products()
print("Вывод данных по магазину:")
Manager.store.showcase()
print("Перегружаем данные из файла и снова выводим на экран:")
Manager.load_data_from_file()
Manager.store.showcase()