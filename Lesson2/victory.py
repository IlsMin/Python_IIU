poet_years = ( ("Пушкин A.C.",     1799),
    ("Цветаева М.И.",   1892),
    ("Маяковский В.В.", 1893),
    ("Высоцкий В.С.",   1938),
    ("Шевчук Ю.Ю.",     1957),
)
cnt = len(poet_years);
while(True):
    print ("Вам нужно будет ввести год рождения поэта. (Всего их", cnt, ")")
    right_answer =0
    for i in range (cnt):
        poet = poet_years[i]
        answer  = int(input(poet[0]+": "))
        if(answer == poet[1]):
            right_answer+=1
   
    right_perc = right_answer/cnt*100.0
   
    print( "Правильных ответов:\t", right_answer, "  (", right_perc, "% )")
    print( "Неверных ответов:\t",   cnt - right_answer,"  (",  100.0 - right_perc, "% )")
    
    if(input("Хотите попробовать снова ? (д/н): ").lower() != "д"): break