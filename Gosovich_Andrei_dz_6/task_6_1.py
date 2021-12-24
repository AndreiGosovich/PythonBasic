
__author__ = "Госович Андрей Михайлович"

# 1.	Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

with open('../nginx_logs.txt', 'r', encoding='utf-8') as nginx_file:
    result_tuple = [(line[:line.index(" ")], line.split('"')[1].split(" ")[0], line.split('"')[1].split(" ")[1])
                    for line in nginx_file]

print(result_tuple[:10])
