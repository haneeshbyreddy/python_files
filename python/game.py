import enum
import turtle

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()
        self.cell_size = 60
        self.screen = turtle.Screen()
        self.screen.setup(width=self._columns * self.cell_size + 100, height=self._rows * self.cell_size + 100)
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.drawGrid()

    def initGrid(self):
        self._grid = [[GridPosition.EMPTY for _ in range(self._columns)] for _ in range(self._rows)]

    def getGrid(self):
        return self._grid

    def getColumnCount(self):
        return self._columns

    def placePiece(self, column, piece):
        if column < 0 or column >= self._columns:
            raise ValueError('Invalid column')
        if piece == GridPosition.EMPTY:
            raise ValueError('Invalid piece')
        for row in range(self._rows-1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                self.drawPiece(row, column, piece)
                return row

    def checkWin(self, connectN, row, col, piece):
        count = 0
        # Check horizontal
        for c in range(self._columns):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check vertical
        count = 0
        for r in range(self._rows):
            if self._grid[r][col] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check diagonal
        count = 0
        for r in range(self._rows):
            c = row + col - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = col - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        return False
    def drawGrid(self):
        self.t.speed(0)  # Speed up the drawing
        self.t.penup()
    
        # Starting position
        start_x = -self._columns * self.cell_size // 2
        start_y = self._rows * self.cell_size // 2
    
        for row in range(self._rows):
            for col in range(self._columns):
                self.t.goto(start_x + col * self.cell_size, start_y - row * self.cell_size)
                self.t.pendown()
                for _ in range(4):
                    self.t.forward(self.cell_size)
                    self.t.right(90)
                self.t.penup()

    def drawPiece(self, row, col, piece):
        self.t.penup()
        x = col * self.cell_size - self._columns * self.cell_size // 2 + self.cell_size // 2
        y = row * self.cell_size - self._rows * self.cell_size // 2 + self.cell_size // 2
        self.t.goto(x, y)
        if piece == GridPosition.YELLOW:
            self.t.color("yellow")
        elif piece == GridPosition.RED:
            self.t.color("red")
        self.t.dot(self.cell_size - 10)

class Player:
    def __init__(self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor

    def getName(self):
        return self._name

    def getPieceColor(self):
        return self._pieceColor

class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore
        self._players = [
            Player(self._grid.screen.textinput("Player 1", "Enter the player 1 name:"), GridPosition.YELLOW),
            Player(self._grid.screen.textinput("Player 2", "Enter the player 2 name:"), GridPosition.RED)
        ]


        

        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0

    def playMove(self, player):
        colCnt = self._grid.getColumnCount()
        while True:
            moveColumn = self._grid.screen.numinput(f"{player.getName()}'s turn", f"Enter column (0-{colCnt - 1}) to add piece: ", minval=0, maxval=colCnt - 1)
            if moveColumn is not None:
                moveColumn = int(moveColumn)
                try:
                    moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
                    return (moveRow, moveColumn)
                except ValueError as e:
                    print(e)

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkWin(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player

    def play(self):
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            self._grid.t.write(f"{winner.getName()} won the round", align="center", font=("Arial", 16, "normal"))
            self._grid.screen.ontimer(2000)
            maxScore = max(self._score[winner.getName()], maxScore)

            self._grid.initGrid()  # reset grid
            self._grid.drawGrid()
        self._grid.t.write(f"{winner.getName()} won the game", align="center", font=("Arial", 16, "normal"))
        self._grid.screen.ontimer(2000)
        exit(1)
        
wn = turtle.Screen()
grid = Grid(6, 7)
game = Game(grid, 4, 2)
game.play()

turtle.done()
wn.mainloop()
