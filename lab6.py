import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        damage = random.randint(0, self.power)
        enemy.health -= damage
        print(f"{self.name} атакує {enemy.name} і завдає {damage} урону.")

    def is_alive(self):
        return self.health > 0

def validate_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Будь ласка, введіть числове значення.")

def create_character():
    name = input("Введіть ім'я персонажа: ")
    health = validate_input("Введіть кількість здоров'я персонажа: ")
    power = validate_input("Введіть силу атаки персонажа: ")
    return Character(name, health, power)

def battle(player1, player2):
    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if not player2.is_alive():
            break
        player2.attack(player1)

    if player1.is_alive():
        print(f"{player1.name} переміг!")
    else:
        print(f"{player2.name} переміг!")

players = {1: None, 2: None}

while True:
    print("\nМеню:")
    print("1. Вибрати героїв для битви")
    print("2. Редагувати героя")
    print("3. Запустити бій")
    print("4. Вийти з програми")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        print("Створення першого гравця:")
        players[1] = create_character()
        print("\nСтворення другого гравця:")
        players[2] = create_character()
    elif choice == "2":
        player_choice = input("Оберіть гравця для редагування (1 або 2): ")
        if player_choice in ('1', '2'):
            print(f"Редагування гравця {player_choice}:")
            name = input("Введіть нове ім'я персонажа: ")
            health = validate_input("Введіть нову кількість здоров'я персонажа: ")
            power = validate_input("Введіть нову силу атаки персонажа: ")
            players[int(player_choice)] = Character(name, health, power)
        else:
            print("Неправильний вибір гравця!")
    elif choice == "3":
        if all(players.values()):
            battle(players[1], players[2])
        else:
            print("Спочатку створіть обох гравців!")
    elif choice == "4":
        print("Дякую за гру!")
        break
    else:
        print("Будь ласка, оберіть вірну опцію.")
