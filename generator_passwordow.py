import random
import string

def generate_password(length, use_digits=True, use_letters=True, use_special_chars=True):
    characters = ""
    
    if use_digits:
        characters += string.digits  # Цифры (0-9)
    if use_letters:
        characters += string.ascii_letters  # Буквы (a-z, A-Z)
    if use_special_chars:
        characters += string.punctuation  # Специальные символы (!@#$%^&* и т.д.)
    
    if not characters:
        characters = string.digits + string.ascii_letters + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Добро пожаловать в генератор паролей!")
    
    try:
        # Запрос количества паролей
        num_passwords = int(input("Сколько паролей вы хотите сгенерировать? "))
        if num_passwords <= 0:
            print("Количество паролей должно быть больше 0.")
            return
        
        # Запрос длины пароля
        length = int(input("Введите длину пароля: "))
        if length <= 0:
            print("Длина пароля должна быть больше 0.")
            return
        
        # Настройка символов
        use_digits = input("Включать цифры (0-9)? (да/нет): ").lower() == 'да'
        use_letters = input("Включать буквы (a-z, A-Z)? (да/нет): ").lower() == 'да'
        use_special_chars = input("Включать специальные символы (!@#$%^&*)? (да/нет): ").lower() == 'да'
        
        # Генерация и вывод паролей
        print("\nВаши пароли:")
        for i in range(num_passwords):
            password = generate_password(length, use_digits, use_letters, use_special_chars)
            print(f"Пароль {i + 1}: {password}")
    
    except ValueError:
        print("Ошибка: введите корректное число.")

if __name__ == "__main__":
    main()