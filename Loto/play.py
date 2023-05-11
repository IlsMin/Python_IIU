import loto_classes as lc
from loto_classes import * #StepGenerator, PlayCard
# steps = StepGenerator()
# print(type(steps))
Cards = []
PLAYERS_CNT = 2
for i in range(PLAYERS_CNT):
    name = 'You' if i==0 else f'Computer_{i}'
    Cards.append(lc.PlayCard(name, i>0))
# lCards.append(lc.PlayCard(, True))
step_gen = lc.StepGenerator()
print(len(Cards))
while(len(Cards)==PLAYERS_CNT):
    val = step_gen.get_next_step()
    print(f'\nНовый бочонок: {val}')
    for card in Cards:
        card.draw_card();

    answer_is_right  =  True
    des = input('Зачеркнуть цифру? (д/н): ').lower()
    if(des == 'д'):
        if(not Cards[0].check_step(val)):
            print (f' Такого числа ({val}) нет на Вашей карте')
            answer_is_right  =  False
        else: Cards[0].mark(val)
    else:
        if(Cards[0].check_step(val)):
            print (f' Такоe чиcло ({val}) есть на Вашей карте')
            answer_is_right  =  False
      
    if(not answer_is_right):
        print('- Вы проиграли')
        Cards.remove(Cards[0])
        break
    
    for i in  range(1,PLAYERS_CNT):
        Cards[1].check_step(val)

    for i in range(1,-1,-1):
        if(Cards[i].is_empty()): 
            print(f'Выиграл: {Cards[i].owner}')
            Cards[i].draw_card();
            Cards.remove(Cards[i])
            
