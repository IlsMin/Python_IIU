import unittest
import numpy as np
import loto_classes as lc

class TestStepGenerator(unittest.TestCase):
    
    def setUp(self):
        self.gener = lc.StepGenerator()
        
    def tearDown(self):
        del self.gener 
        
    def test_lc_init(self):
        assert (len(self.gener.cells) == 1)
        assert (self.gener.cells[0]==0)
    
    def test_lc_init2(self):
        # gener = lc.StepGenerator()
        self.assertEqual (len(self.gener.cells), 1)
        self.assertEqual (self.gener.cells[0], 0)
        print('cells1', self.gener.cells)


    def test_lc_over(self):
        # gener = lc.StepGenerator() # 1 item =0 already exists!
        for i in range(1, self.gener.CELLS_COUNT):
            self.gener.get_next_step()
        self.assertEqual(len(self.gener.cells),2)       
        print(self.gener.cells)
        self.gener.get_next_step()
        self.assertEqual(len(self.gener.cells),3)    
class TestPlayCard(unittest.TestCase):
    
    def setUp(self):
        self.testName = 'Name'  
        self.card = lc.PlayCard(self.testName)
    
    def test_card_init(self):       
        self.assertFalse(self.card.is_empty())
        self.assertFalse(np.any(self.card.tiles, where= self.card.tiles <= 0 ))
        self.assertTrue(np.any(self.card.tiles, where= self.card.tiles > 0 ))
        self.assertEqual(self.testName, self.card.owner)

    def test_card_check(self):

        ar0 = self.card.tiles[self.card.tiles>0][0] # first none zero item
        self.assertTrue(self.card.check_step(ar0))
       
        # print (ar0)
    def test_card_mark(self):
        ar0 = self.card.tiles[self.card.tiles>0][0] # first none zero item
        
        self.assertTrue (self.card.check_step(ar0))
        self.assertTrue (self.card.      mark(ar0))
        self.assertFalse(self.card.check_step(ar0))
# testing computer player
        self.card = lc.PlayCard(self.testName, True)
        ar0 = self.card.tiles[self.card.tiles>0][0] # first none zero item
        
        self.assertTrue (self.card.check_step(ar0)) # comp_player need to mark it !
        self.assertFalse(self.card.check_step(ar0))



