import string


FILE = 'repeated_words.txt'

f = open(FILE, 'w', encoding='utf-8')

mail = ('Когда нам выпадает испытание, мы зачастую встречаем его с гневом и отчаянием, возмущаясь несправедливостью '
        'происходящего. Но гнев делает нас глухими, а отчаяние слепыми. И мы упускаем возможность подняться и вырасти. '
        'И удары и поражения начинают сыпаться на нас со всех сторон. Это не означает, что судьба на нас ополчилась, '
        'это означает, что жизнь снова и снова пытается пробиться к нам со своим посланием.')
f.write(mail)

f.close()


def get_words(file_name):
        with open(file_name, 'r', encoding='utf-8') as text:
                data = text.readline()
                new_data = str(data).split()
                table_punctuation = str.maketrans((dict.fromkeys(string.punctuation)))
                words = str(new_data).translate(table_punctuation).split()
                # print(data)
                # print(words)

                return words

def get_words_dict(file_name):
        unique_words_dict = {}
        for word in get_words(file_name):
                if word in unique_words_dict:
                        unique_words_dict[word] += 1
                else:
                        unique_words_dict[word] = 1
        # print(unique_words_dict)
        return unique_words_dict

def len_words():
        quantity_words = len(get_words(file_name))
        # print(quantity_words)
        return quantity_words

def len_unique_words():
        unique_words = len(get_words_dict(file_name))
        # print(unique_words)
        return unique_words

def print_unique_words():
        info = list(get_words_dict(FILE).items())
        print('Все использованные слова: ')
        for item in info:
                print(f'{item[0]} {item[1]}')


if __name__ == '__main__':
        file_name = input('Введите название файла: ')
        print(f'Количество слов: {len_words()}')
        print(f'Количество уникальных слов: {len_unique_words()}')
        print_unique_words()
