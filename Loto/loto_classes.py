import random
import numpy as np

#  генератор ходов
class StepGenerator:
    CELLS_COUNT = 90
    #cells = []
    def resetCells(self):
        self.cells = []
        self.cells.append(0)
        
    def __init__(self) -> None:
        self.resetCells()
    
    def  get_next_step(self)->int:
        cell = 0
        count = len(self.cells)
        while(cell in self.cells):
            cell = random.randint(1, StepGenerator.CELLS_COUNT)
        count += 1
        if(count >= StepGenerator.CELLS_COUNT):
             print("мешок пуст!\nновый раунд!!")
             self.resetCells()
        self.cells.append(cell)
        return cell
       
        
# карточка
class PlayCard:
    ROW_CNT = 3
    COL_CNT = 8
    # name_l  = 0
    

    def __init__(self, owner, is_auto = False) -> None:
        self.owner = owner if isinstance(owner, str) else 'unknown'
        self.name_l = len ( self.owner)
        self.auto_play = is_auto
        self.tiles = np.zeros((PlayCard.ROW_CNT, PlayCard.COL_CNT),int)
        
        for r in range(PlayCard.ROW_CNT):
            for c in range(5):
                # cell_indx = 0
                while True:
                    cell_indx = random.randint(0, PlayCard.COL_CNT -1)
                    if(self.tiles[r,cell_indx] == 0): break
                val = 0
                while val in self.tiles:
                    val = random.randint(1, StepGenerator.CELLS_COUNT)
                self.tiles[r,cell_indx] = val
   
    def mark(self, val):
        if(not val in self.tiles):
            return False
        
        indexes = np.where(self.tiles == val)# [0]
        # print(indexes)
        self.tiles[indexes] = -1
        return True

    def check_step(self, val):
        exist = val in self.tiles
        if(exist and self.auto_play):
            self.mark(val)
        return exist    
    
    def  is_empty(self):
         # print (np.any(self.tiles, where= self.tiles > 0 ))
        return    not np.any(self.tiles, where= self.tiles > 0 )

    def draw_card(self):
  # TODO    player name in the middle
        # name_l = len ( self.owner)
        width = 4*PlayCard.COL_CNT
        len = (width - self.name_l)//2
        
        print ('-'* (len),end ="")
        print (self.owner,end ="")
        if self.name_l% 2 != 0: len+=1 
        print ('-'* (len))
        for r in range(PlayCard.ROW_CNT):
            for c in range(PlayCard.COL_CNT):
                  if(self.tiles[r,c]== 0):
                    print (' '*3, end=' ')
                  elif self.tiles[r,c] < 0:
                    print (' - ', end=' ')
                  else:
                    print ('{:3d}'.format(self.tiles[r,c]), end=' ')
            print('')
        print ('-'* width)
                
    # if _name__ == '__main__':
    #      run