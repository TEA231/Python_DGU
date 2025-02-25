import random
import requests

def draw_hangman(attempts):
    """
    Рисует виселицу в зависимости от количества оставшихся попыток.
    """
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    print(stages[attempts])

def choose_word():
    """
    Выбирает случайное слово из списка.
    """
    return requests.get("https://random-word-api.herokuapp.com/word").json()[0]

def display_word(word, guessed_letters):
    """
    Отображает слово, заменяя неизвестные буквы на '_'.
    """
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    """
    Основная функция игры "Виселица".
    """
    word = choose_word()  # Выбор случайного слова
    guessed_letters = set()  # Множество угаданных букв
    attempts = 6  # Количество попыток
    print("Добро пожаловать в игру 'Виселица'!")

    while attempts > 0:
        print("\nСлово:", display_word(word, guessed_letters))
        print(f"Осталось попыток: {attempts}")
        draw_hangman(attempts)

        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Правильно! Эта буква есть в слове.")
        else:
            print("Неправильно! Такой буквы нет в слове.")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nПоздравляем! Вы угадали слово:", word)
            break

    if attempts == 0:
        draw_hangman(attempts)
        print("\nВы проиграли! Загаданное слово было:", word)

if __name__ == "__main__":
    hangman()