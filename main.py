import random
import string

#lenght это длинна пароля которую можно менять
def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#adjectives и nouns можете дописывать по желанию
adjectives = [
    "Dark", "Silent", "Furious", "Epic", "Mysterious", "Brave", "Ancient", "Eternal", 
    "Swift", "Frozen", "Mighty", "Crimson", "Stormy", "Golden", "Enchanted", "Shadowy", 
    "Lunar", "Celestial", "Thunder", "Mystic", "Savage", "Iron", "Vengeful", "Clever"
]
nouns = [
    "Wolf", "Knight", "Fox", "Dragon", "Shadow", "Phoenix", "Tiger", "Lion", "Viper", 
    "Hawk", "Eagle", "Panther", "Bear", "Falcon", "Samurai", "Ghost", "Wizard", "Raven", 
    "Reaper", "Golem", "Hunter", "Sage", "Warrior", "Guardian", "Nomad", "Ninja", "Specter"
]
numbers = range(10, 100) #можете поменять для изменения генерации чисел в нике


def generate_nickname():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.choice(numbers)
    nickname = f"{adjective}{noun}{number}"
    return nickname


def ask_yes_no(question):
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()
        if answer in ['y', 'n']:
            return answer
        else:
            print("Пожалуйста, введите 'y' или 'n'.")


txt = ask_yes_no("Записать ли данные в файл ?")


if txt == 'y':
    nfile = str(input('Введите название файла:'))
    num = int(input('Введите число генерируемых аккаунтов:'))

    with open(f'{nfile}.txt', "w") as file:
        for _ in range(num):
            login = generate_nickname()
            password = generate_password(20)
            file.write(f"{login}:{password}\n")

    print(f"Данные успешно записаны в файл {nfile}.txt")
elif txt == 'n':
    num = int(input('Введите число генерируемых аккаунтов:'))

    for _ in range(num):
        login = generate_nickname()
        password = generate_password()
        print(f"{login}:{password}")
else:
    pass


#⢰⣶⣼⣿⣷⣿⣽⠿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣷⡀⠛⢿⣿
#⢃⣺⣿⣿⣿⢿⠏⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣿⣿⣷⢹⣿⣷⣄⠄⠈
#⡼⣻⣿⣷⣿⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⠸⣿⣿⣿⣿⣶
#⣇⣿⡿⣿⠏⣸⣎⣻⣟⣿⣿⣿⢿⣿⣿⣿⣿⠟⣩⣼⢆⠻⣿⡆⣿⣿⣿⣿⣿
#⢸⣿⡿⠋⠈⠉⠄⠉⠻⣽⣿⣿⣯⢿⣿⣿⡻⠋⠉⠄⠈⠑⠊⠃⣿⣿⣿⣿⣿
#⣿⣿⠄⠄⣰⠱⠿⠄⠄⢨⣿⣿⣿⣿⣿⣿⡆⢶⠷⠄⠄⢄⠄⠄⣿⣿⣿⣿⣿
#⣿⣿⠘⣤⣿⡀⣤⣤⣤⢸⣿⣿⣿⣿⣿⣿⡇⢠⣤⣤⡄⣸⣀⡆⣿⣿⣿⣿⣿
#⣿⣿⡀⣿⣿⣷⣌⣉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣌⣛⣋⣴⣿⣿⢣⣿⣿⣿⣿⡟
#⢹⣿⢸⣿⣻⣶⣿⢿⣿⣿⣿⢿⣿⣿⣻⣿⣿⣿⡿⣿⣭⡿⠻⢸⣿⣿⣿⣿⡇
#⠈⣿⡆⠻⣿⣏⣿⣿⣿⣿⣿⡜⣭⣍⢻⣿⣿⣿⣿⣿⣛⣿⠃⣿⣿⣿⣿⡿⠄
#⣦⠘⣿⣄⠊⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⡿⠁⠄