from gameboard import Gameboard
from random import randint

class ComputerBoard(Gameboard):
     # NUMSHIPS = 5
     def place_comp_ships(self):
        width = len(self.data[0])
        height = len(self.data)
        ship_placed = False
        x = randint(0, width-1)
        y = randint(0, height-1)
        orient = randint(0,2)
        size = 5
        while ship_placed == False:
            for i in range(size-1, -1, -1):
                if x+i >= width or y+i >= height or self[x+i,y] == 'S' or self[x,y+i] == 'S':
                    x = randint(0, width-1)
                    y = randint(0, height-1)
                else:
                    ship_placed = True
        for j in range(size-1,-1,-1):
            if orient == 0:
                self[x+j,y] = 'S'    
            elif orient == 1:
                self[x,y+j] = 'S'
                    
            
        # while ship_placed == False:
        #     if orient == 1:
        #         for i in range(size-1, -1, -1):
        #             if self[x+i, y] == 'S' or x+i >= width:
        #                 x = randint(0, width-1)
        #                 y = randint(0, height-1)
        #                 #clear board of S's                        
        #             else:
        #                 self[x+i, y] = 'S'
        #     else:
        #         for j in range(size-1, -1, -1):
        #             if self[x, y+j] == 'S' or y+j >= height:
        #                 x = randint(0, width-1)
        #                 y = randint(0, height-1)     
        #             else:
        #                 self[x, y+j] = 'S'    
        #     if self.count_symbol('S') == 5:
        #         ship_placed = True
                
                    
                
            
            
            #     else:
            #         for j in range(size-1,0):
            #             if self[x, y+j] == 'S':
            #                 break
            #             else:
            #                 self[x, y+j] = 'S'
            #             return False
            #         break
                    
            # except ValueError:
            #     break
            # return False
            

# if orient == 1:
#             for i in range(size + 1):
#                 self[x+i, y] = "S"
#         if orient == 2:
#             for i in range(size + 1):
#                 self[x, y+i] = "S" 
    
    # def place_random_ships(self):
    #     width = len(self.data[0])
    #     height = len(self.data)
    #     x = randint(0, width-1)
    #     y = randint(0, height-1)
    #     o = randint(1,2)
    #     destroyer = ComputerBoard().place_ship(x, y, size=2, orient=o)
    #     while destroyer == False:
    #         destroyer
    
     
