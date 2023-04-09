year = 0
while(year != 1799):
    year = int(input ("Год рождения А.С.Пушкина? "))
#6 июня 1799
    if(year != 1799):
        print ("Неверно")
    else:
        print("Верно")
        break
real_day =  "6 июня"   
day = ""
while(day != real_day):
    day = input ("день (и месяц) рождения А.С.Пушкина? ")

    if(day != real_day):
        print ("Неверно")
    
print ("Верно")