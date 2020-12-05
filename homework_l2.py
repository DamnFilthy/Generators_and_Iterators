import requests
import json
import os
from pprint import pprint
import hashlib


# Класс итератора, который возвращает список стран
class Downloader:
    def __init__(self, file_name):
        self.file_name = file_name

    def iterator(self):
        with open(self.file_name) as file:
            country_names = []
            data = json.loads(file.read())
        for i, name in enumerate(data):
            country_names.append(data[i]['name']['common'])
        return country_names


# генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
def hash_generate(my_path):
    files = (os.listdir(my_path))
    print(files)
    for file in files:
        if file.endswith('.json'):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.readlines()
                clear_content = [x.strip() for x in content]
                for line in clear_content:
                    yield hashlib.md5(line.encode('utf-8')).hexdigest()


if __name__ == '__main__':

    # Используем итератор
    my_file = Downloader('countries.json').iterator()
    with open('wiki_country.txt', 'w', encoding='UTF-8') as f:
        link = 'wikipedia.org/wiki/'
        result = []
        for country in my_file:
            new_link = link + country + '\n'
            result = country + ' : ' + new_link
            f.write(result)

    # Используем генератор
    for country in hash_generate('C:\\Users\\User\\Desktop\\my_files'):
        print(country)
