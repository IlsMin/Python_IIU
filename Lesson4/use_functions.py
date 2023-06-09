"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import json
import os

HIST_FILE_NAME = 'history.json'
history =[]
account_sum = 0.0

def add_sum(sum):
    global account_sum
    account_sum += sum

def check_sum(sum):
   # global glob_sum 
    if(sum > account_sum):
        print(f" Остаток на Вашем счету ({ account_sum}) не позволяет оформить покупку ")
        return False
    
    return True

def buy(sum, good):
    if(not check_sum(sum)):
        return False
    global account_sum
    account_sum -= sum
  #  global history
    history.append((good,sum))
    return True

def print_history():
    print(*history, sep='\n')
    

def write_to_file():
    jsonval = {'hist': history, 'sum': account_sum}
    with open(HIST_FILE_NAME, "w") as f:
        json.dump(jsonval, f)

def read_from_file():
    if os.path.isfile(HIST_FILE_NAME) and os.path.getsize(HIST_FILE_NAME) > 0:
        with open(HIST_FILE_NAME, "r") as f:
            jsonval = json.load(f)
        global history
        history = jsonval['hist']
        global account_sum
        account_sum = jsonval['sum']
    
    else: print(f"No {HIST_FILE_NAME} file or it's empty")

def run_bank():
    if(os.path.exists(HIST_FILE_NAME)):
        read_from_file()
        # print_history()

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. запись в файлы')
        print('5. выход')

       
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            sum = float(input(' Введите сумму пополнения: '))
            if (sum >0.0):
                add_sum(sum)
        elif choice == '2':
            sum = float(input(' Введите цену покупки: '))
            if (check_sum(sum)):
                good= input(' Введите  наименование товара/услуги: ')
                buy(sum, good)
           
        elif choice == '3':
            print_history()

        elif choice == '4':
            write_to_file()

        elif choice == '5':
            write_to_file()
            break
        else:
            print('Неверный пункт меню')

if __name__ == "__main__":
    run_bank()
