
__author__ = "Госович Андрей Михайлович"

# 2.	*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('../nginx_logs.txt', 'r', encoding='utf-8') as nginx_file:
    dict_ip = {}
    for line in nginx_file:
        remote_addr = line[:line.index(" ")]
        if remote_addr in dict_ip:
            dict_ip[remote_addr] += 1
        else:
            dict_ip[remote_addr] = 1

spammers = sorted(dict_ip.items(), key=lambda x: x[1], reverse=True)[0:4]
for spammer in spammers:
    print(f"СПАМер: {spammer[0]}, кол-во запросов: {spammer[1]}")

