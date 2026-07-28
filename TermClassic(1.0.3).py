import time
import random
import os

name = None
password = None
selected_command = None
is_registered = False
os_name = "Terminal Classic"
start_time = time.time()
quotes_number  = ["Memento Mori", "Код - это поэзия.", "Скоро все  о тебе забудет, и сам ты забудешь о себе."]


print(f"Добро пожаловать в Terminal Classic!")
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
    print("4. help - показывает команды. ")
    print("5. time - показывает точное время и месяц на данный момент. ")
    print("6. clear - очищает экран терминала. ")
    print("7. date - показывает текущую дату терминала. ")
    print("8. echo - вывод любого текста. ")
    print("9. calc - компактный современный калькулятор в терминале. ")
    print("10. info - показыает информацию о системе.")
    print("11. ping - показывает текущую время задержку.")
    print("12. restart - перезапускает и очищает кэш ОС. ")
    print("13. quotes  - показывает цитаты. ")
    print("14. uptime - показывает время сессии терминала.")
    print("15. exit - закрывает текущую сессию терминала")
    
def cmd_uptime():
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60
    print(f"Терминал открыт: {minutes} мин {seconds} сек")
    
def info():
  print("=================")
  print("Информация о системе: ")
  print(f"Пользователь {name}. ")
  print("Текущая версия Terminal Classic:  - 1.0.3")
  print(f"ОС - {os_name}")
  print("Количество команд - 15")
  print("Автор: X7legendv2")
  print("Архитектура - AMD64,X86")
  print("=================")  
  
def cmd_quotes():
   print(random.choice(quotes_number))
    
def calc():
  print("Исходный калькулятор")
  num1 = float(input("Введите первое число: "))
  num2 = float(input("Введите второе число: "))
  op = input("Выберите операцию: +, -, *, /")
  
  if op == "+":
   print(num1 + num2)
  elif op == "-":
   print(num1 - num2)
  elif op == "*":
   print(num1 * num2)
  elif op == "/":
   print(num1 / num2)
  else:
   print("Неверная операция.")
   
def os_restart():
  print("Перезапуск Терминала 1.0.3")
  restart = input("Вы согласны? Нажмите 1 для выполнение команды. ")
  
  if restart == "1":
    print("Перезапуск..")
    time.sleep(2)
    print("Успешный перезапуск ОС Terminal Classic! ")
  else:
      print("Отказано. ")

def cmd_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_loop():
    global name, plasma

    while True:
        cmd_comm = input("Выберите команду (1-15): ").strip()

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
            print(f"Дата: {time.strftime('%d.%m.%Y')}")
        elif cmd_comm == "8":
          text = input("Введите текст: ")
          print(text)
        elif cmd_comm == "9":
         calc()
        elif cmd_comm == "10":
          info()
        elif cmd_comm == "11":
          ping = random.randint(1,200)
          print(f"Время задержки:  {ping} мс ")
        elif cmd_comm == "12":
            os_restart()
        elif cmd_comm == "13":
          cmd_quotes()
        elif cmd_comm == "14":
          cmd_uptime()
        elif cmd_comm == "15":
          print("Выход из текущей сессии...")
          time.sleep(3)
          print(f"Выход осуществлен {name} ")
          break
        else:
          print("Неверная команда, нажмите 4 для подробностей. ")
         

# --- ЗАПУСК ---
register()

if is_registered:
    print(f"Добро пожаловать, {name}!")
    time.sleep(1)
    show_commands()
    game_loop()
else:
   print("Вы ещё не зарегистрированы!")