import random

def guess_number():
    secret_number = random.randint(11, 100)
    
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 11 до 100. Попробуйте угадать его!")

    while True:
        try:
            guess = int(input("Введите ваше число: "))
            
            if guess < secret_number:
                print("Слишком мало, попробуйте еще раз.")
            elif guess > secret_number:
                print("Слишком много, попробуйте еще раз.")
            else:
                print("Вы угадали, поздравляем!")
                
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_number()