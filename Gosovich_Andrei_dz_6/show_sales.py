
__author__ = "Госович Андрей Михайлович"

# 6.	Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# ●	просто запуск скрипта — выводить все записи;
# ●	запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# ●	запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

import sys

with open("bakery.csv", "r", encoding="utf-8") as sales_file:
    if len(sys.argv) == 1:
        print(sales_file.read())
    elif len(sys.argv) == 2 and sys.argv[1].isnumeric():
        i = 52 * (int(sys.argv[1]) - 1)
        sales_file.seek(i)
        for line in sales_file:
            print(line.strip())
            i += 52
    elif len(sys.argv) == 3 and sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
        i = 52 * (int(sys.argv[1]) - 1)
        sales_file.seek(i)
        for line in sales_file:
            if i <= (int(sys.argv[2]) - 1) * 52:
                print(line.strip())
            else:
                break
            i += 52
