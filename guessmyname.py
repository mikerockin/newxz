name = 'Mike'
running = True
while running:
    guess = (input('Угадайте моё имя из 4 букв : '))
    if guess == name:
        print('Поздравляю, Вы угадали, меня зовут Mike')
        print('А как зовут Вас? ')
        guestname = input()
        print('Приветствую тебя' , guestname,'!')
        running = False
    elif guess != name:
        print('Последняя буква е')
        break
while running:
    guess = (input('Угадайте моё имя из 4 букв : '))
    if guess == name:
        print('Поздравляю, Вы угадали, меня зовут Mike')
        print('А как зовут Вас? ')
        guestname = input()
        print('Приветствую тебя' , guestname,'!')
        running = False
    elif guess != name:
        print('Первая буква M')
        break
while running:
    guess = (input('Угадайте моё имя из 4 букв : '))
    if guess == name:
        print('Поздравляю, Вы угадали, меня зовут Mike')
        print('А как зовут Вас? ')
        guestname = input()
        print('Приветствую тебя' , guestname,'!')
        running = False
    elif guess != name:
        print('Вторая буква моего имени i')
        break
while running:
    guess = (input('Осталось угадать всего 1 букву Mi_e : '))
    if guess == name:
        print('Поздравляю, Вы угадали, меня зовут Mike')
        print('А как зовут Вас? ')
        guestname = input()
        print('Приветствую тебя' , guestname,'!')
        running = False
