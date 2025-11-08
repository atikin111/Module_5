import itertools


def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♥', '♦', '♣', '♠']

    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank}{suit}')

    return deck

def generate_combinations(num_card, deck):
    if num_card < 1 or num_card > 52:
        print('Количество карт должно быть от 1 до 52')
        return []

    combinations = list(itertools.combinations(deck, num_card))
    return combinations

def main():
    deck = create_deck()
    print(f'Создана колода: {deck}')

    try:
        num_card = int(input('Введите количество карт для комбинаций от 1 до 52: '))
    except ValueError:
        print('Введите целое число')
        return

    combinations = generate_combinations(num_card, deck)
    if not combinations:
        return
    save_info(num_card, combinations)

def save_info(num_card, combinations):
    choice = input('Выберите действие: '
                   '\n1 - Вывести все комбинации на экран'
                   '\n2 - Сохранить в файл'
                   '\n3 - Вывести только количество комбинаций'
                   '\nВаш выбор: ')

    if choice == '1':
        print(f'Все комбинации из {num_card} карт: ')
        for i, combo in enumerate(combinations, 1):
            print(f'{i}. {combo}\n')

    elif choice == '2':
        filename = 'card_combinations.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'Комбинации из {num_card} карт (всего: {len(combinations)}')
            for i, combo in enumerate(combinations, 1):
                f.write(f'{i}. {combo}\n')
        print(f'Результаты сохранены в файл: {filename}')

    elif choice == '3':
        print(print(f'Количество комбинаций из {num_card} карт: {len(combinations)}'))

    else:
        print('Неверный выбор')

if __name__ == '__main__':
    main()