import time
import random
import os

name = None
password = None
selected_command = None
is_registered = False


print("Добро пожаловать в Terminal Classic!")
time.sleep(1)
print("Необходимо зарегистрироваться.")
time.sleep(1)

def register():
    global name, password, is_registered
    name = input("Создайте имя: ")
    password = input("Создайте пароль: ")
    is_registered = True
    print(f"Пользователь {name} создан!")

def show_commands():
    print("==============")
    print("Доступные команды: ")
    print("1. whoami - показывает текущего пользователя.")
    print("2. plasma - генерирует случайное число.")
    print("3. bit - показывает много чисел.")
    print("4. help - показывает команды.")
    print("5. time - показывает точное время и месяц на данный момент.")
    print("6. clear - очищает экран терминала.")
    print("7. exit - закрывает текущую сессию терминала.")

def cmd_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_loop():
    global name, plasma

    while True:
        cmd_comm = input("Выберите команду (1-7): ").strip()

        if cmd_comm == "1":
            print(name)
        elif cmd_comm == "2":
            plasma = random.randint(1,16)
            print(plasma)
        elif cmd_comm == "3":
            for i in range(1, 11):
                print(i * 3, end=" ")
            print()
        elif cmd_comm == "4":
            show_commands()
        elif cmd_comm == "5":
            print(f"Время: {time.strftime('%H:%M')}")
            print(f"Месяц: {time.strftime('%B')}")
        elif cmd_comm == "6":
            cmd_clear()
        elif cmd_comm == "7":
            print("Выход из текущей сессии...")
            time.sleep(1)
            print(f"Выход осуществлен, {name}")
            break
        else:
          print("Неизвестная команда, нажмите 4 для подробностей")
              
          

# --- ЗАПУСК ---
register()

if is_registered:
    print(f"Добро пожаловать, {name}!")
    time.sleep(1)
    show_commands()
    game_loop()
else:
    print("Вы ещё не зарегистрированы!")
