import string

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with (open(file_name, 'r', encoding='utf-8') as n_file):
                file_str = n_file.read().lower()
                str_punk = str.maketrans(',', ',', string.punctuation + '-')
                file_str = file_str.translate(str_punk)
                all_words[file_name] = file_str.split()

            return all_words

    def find(self, word):
        position = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                position[key] = value.index(word.lower()) + 1
        return position

    def count(self, word):
        counter = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counter[value] = words_count
        return counter


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего