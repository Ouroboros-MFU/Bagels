from random import randint

NUM_DIGITS = 3
MAX_GUESSES = 10


print(f'''Багелс, дедуктивно логическая игра.
By Danil Egorikov.
Я загадал {NUM_DIGITS}-значное число. Попробуй его угадать.
Тут есть несколько подсказок:
Когда я говорю: Это подсказки:
 Pico Одна цифра правильная, но не на своем месте.
 Fermi Одна цифра правильная и находится на своем месте.
 Bagels Нет правильных цифр.
Я загадал число.
У тебя есть {MAX_GUESSES} попыток, чтобы угадать.
 Удачи!''')
def main():
    count = 0
    while True:
        digit = str(get_random())

        num_guess = 1
        while num_guess <= MAX_GUESSES:
            print(f'Попытка №{num_guess}: Введите число ')
            guess = input('>')
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Попытка №{num_guess}: не верный формат, повторите ввод')
                guess = input(">")
            print(position(digit, guess))
            num_guess += 1

            if guess == digit:
                break
            if num_guess > MAX_GUESSES:
                print(f'Попытки закончились, правильное число было: {digit}')
        print('Вы хотите сыграть снова? (yes/no)')
        if not input().lower().startswith('y'):
            break
    print("Спасибо за игру!")








def get_random():
    random = randint(100, 999)
    return random


def position(random, guess):
    if random == guess:
        return "Вы угадали!"
    clues = []
    for i in range(NUM_DIGITS):
        if (guess[i] == random[i]):
            clues.append('Fermi')
        elif (guess[i] in random):
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    main()
