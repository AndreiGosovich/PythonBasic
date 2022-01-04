
__author__ = "Госович Андрей Михайлович"

#2.	*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>,
# <requested_resource>, <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re

RE_LOG_RECORD = re.compile(r'^(?P<remote_addr>[\d, \.]+|.*:.+)\b.*[\[]'
                           r'(?P<request_datetime>.+)[\]]\s["]'
                           r'(?P<request_type>\w+)\s'
                           r'(?P<requested_resource>.+) .+"\s'
                           r'(?P<response_code>\d+)\s'
                           r'(?P<response_size>\d+)')

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    log_list = []
    for raw in f:
        parsed_raw = RE_LOG_RECORD.findall(raw)[0]
        log_list.append(parsed_raw)

print(log_list[:10])
