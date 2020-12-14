import requests
import json
import os
import hashlib


# Задание №1
# Класс итератора, который возвращает список стран
class Downloader:
    def __init__(self, file_name):
        self.file_name = open(file_name)
        self.data = json.loads(self.file_name.read())
        self.counter = -1
        self.country_names = []
        for i, name in enumerate(self.data):
            self.country_names.append(self.data[i]['name']['common'])

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.country_names):
            raise StopIteration
        return self.country_names[self.counter]


# Задание №2
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
    # Задание №1
    # Используем итератор
    with open('wiki_country.txt', 'w', encoding='UTF-8') as f:
        data = Downloader('countries.json')
        link = 'wikipedia.org/wiki/'
        result = []
        for country in data:
            new_link = link + country + '\n'
            result = country + ' : ' + new_link
            f.write(result)

    # Задание №2
    # Используем генератор
    for country in hash_generate('C:\\Users\\User\\Desktop\\my_files'):
        print(country)
