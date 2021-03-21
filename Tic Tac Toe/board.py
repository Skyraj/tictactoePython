class Board:
    def __init__(self):
        self.grid = [['','',''],['','',''],['','','']]
    
    def check(self):
        if self.grid[0][0] != '' and self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]:
            pass
        elif self.grid[0][0] != '' and self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]:
            pass