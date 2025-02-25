def caesar_cipher(text, shift, language, direction):
    if language == 'ru':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # Русский алфавит (32 буквы)
        alphabet_upper = alphabet.upper()
    elif language == 'en':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Английский алфавит
        alphabet_upper = alphabet.upper()
    else:
        raise ValueError("Неподдерживаемый язык. Используйте 'ru' или 'en'.")

    result = []

    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet) if direction == 'шифрование' else (index - shift) % len(alphabet)
            result.append(alphabet[new_index])
        elif char in alphabet_upper:
            index = alphabet_upper.find(char)
            new_index = (index + shift) % len(alphabet_upper) if direction == 'шифрование' else (index - shift) % len(alphabet_upper)
            result.append(alphabet_upper[new_index])
        else:
            result.append(char)

    return ''.join(result)

def main():
    print("Добро пожаловать в программу шифрования Цезаря!")

    direction = input("Выберите направление (шифрование/дешифрование): ").lower()
    if direction not in ['шифрование', 'дешифрование']:
        print("Ошибка: направление должно быть 'шифрование' или 'дешифрование'.")
        return
    
    language = input("Выберите язык алфавита (ru/en): ").lower()
    if language not in ['ru', 'en']:
        print("Ошибка: язык должен быть 'ru' или 'en'.")
        return
    
    try:
        shift = int(input("Введите шаг сдвига (целое число): "))
    except ValueError:
        print("Ошибка: шаг сдвига должен быть целым числом.")
        return
    
    text = input("Введите текст: ")
    
    result = caesar_cipher(text, shift, language, direction)
 
    print("\nРезультат:")
    print(result)

if __name__ == "__main__":
    main()