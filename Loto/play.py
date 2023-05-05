import loto_classes as lc
from loto_classes import * #StepGenerator, PlayCard
# steps = StepGenerator()
# print(type(steps))
Cards = []
Cards.append(lc.PlayCard('You'))
Cards.append(lc.PlayCard('Computer', True))
step_gen = lc.StepGenerator()
print(len(Cards))
while(True): #len(Cards)==2):
    val = step_gen.get_next_step()
    print(f'\nНовый бочонок: {val}')
    for card in Cards:
        card.draw_card();

    des = input('Зачеркнуть цифру? (д/н): ').lower()
    if(des == 'д'):
        if(not Cards[0].check_step(val)):
            print (f' Такого чила ({val}) нет на Вашей карте - Вы проиграли')
            exit
        else: Cards[0].mark(val)
    else:
        if(Cards[0].check_step(val)):
            print (f' Такоe чиcло ({val}) есть на Вашей карте - Вы проиграли')
            exit
    Cards[1].check_step(val)
    for i in range(1,-1,-1):
       if(Cards[i].is_empty()): 
         print(f'Выиграл: {Cards[i].owner}')
        #  Cards.remove(Cards[i])
         break

  


