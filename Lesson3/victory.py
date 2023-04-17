import random
#from datetime import datetime

def get_stringed_BD(bd):
    bd_parts = bd.split('.')
    if(len(bd_parts) !=3):
        print ("неверный формат даты! Должен быть : дд.мм.гггг")
        return ''
    for i in range(3):
        if(len(bd_parts[i]) < 2):
            print ("неверный формат даты! Должен быть : дд.мм.гггг - c лидирующими нулями для малых чисел" )
            return ''
        bd_parts[i] = int(bd_parts[i])
        if(i <2):  bd_parts[i]-=1  #zero index
     # check day and month       
    if(bd_parts[0] < 1 or bd_parts[0] >31):
        print ("неверный день даты! (Формат : дд.мм.гггг)")
        return ''
    if(bd_parts[1] < 1 or bd_parts[1] >12):
        print ("неверный месяц даты! (Формат : дд.мм.гггг)")
        return ''
 
    monthes = ("января", "февраля", "марта", "апреля", "мая", "июня",
               "июля","августа","сентября", "октября","ноября","декабря"
             )
    #https://ru.stackoverflow.com/questions/623775/%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B0%D1%82%D1%8B-%D0%BF%D1%80%D0%BE%D0%BF%D0%B8%D1%81%D1%8C%D1%8E-%D0%BD%D0%B0-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC-%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5
    days = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 
        'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадацать четвёртое', 'двадцать пятое',
        'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое',
        'тридцать первое']
    
    return ( f'{ days[bd_parts[0]]} {monthes[bd_parts[1]]} { bd_parts[2] } года')
    
def run_victory():
    #https://worldtable.info/literatura/tablica-gody-zhizni-russkih-pisatelei-i-poyet.html
    poet_years = (
        ("Пушкин A.C.",      '26.05.1799'),
        ("Цветаева М.И.",    '08.10.1892'),
        ("Маяковский В.В.",  '07.07.1893'),
        ("Высоцкий В.С.",    '25.01.1938'),
        ("Шевчук Ю.Ю.",      '16.05.1957'),
        ("Блок А.А.",        '16.11.1980'),
        ("Белый А.Н.",       '14.10.1880'),
        ("Есенин С.А.",      '21.09.1895'),
        ("Лермонотов М.Ю.",  '03.10.1814'),
        ("Мандельштам О.Э.", '03.01.1891'),
        ("Вознесенский А.А.",'12.05.1933')
        )
     
    poet_rand = random.sample(poet_years,5)
    cnt = len(poet_rand);
    while(True):
        print ("Вам нужно будет ввести дату рождения поэта в формате 'дд.мм.гггг'. (Всего поэтов:", cnt, ")")
        right_answer =0
        for poet in poet_rand:
            #print(poet, type(poet))
            #hole = type(poet)
            answer  = input(poet[0]+": ")
            if(answer == poet[1]):
                right_answer+=1
            else:
                check =  get_stringed_BD(answer)
                if len(check) == 0:
                    continue;
                print("верный ответ:", get_stringed_BD(poet[1]))
       
        right_perc = right_answer/cnt*100.0
       
        print( "Правильных ответов:\t", right_answer, "  (", right_perc, "% )")
        print( "Неверных ответов:\t",   cnt - right_answer,"  (",  100.0 - right_perc, "% )")
        
        if(input("Хотите попробовать снова ? (д/н): ").lower() != "д"): break

if __name__ == "__main__":
    run_victory()
