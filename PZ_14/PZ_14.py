# В исходном текстовом файле (radio_stations.txt) найти все домены из URL-адресов.

import re

def main():
    # Открываем файл на чтение
    f1 = open("radio_stations.txt", "r", encoding='utf-8')
    radio_stations = f1.read()
    # Ищем домены
    domains = re.findall("https?://([\w\-_.]+).*", radio_stations)
    print(domains)

if __name__ == '__main__':
    main()
