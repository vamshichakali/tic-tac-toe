import random
board=["-","-","-",
      "-","-","-",
      "-","-","-"]
currentplayer="X"
winner=None
gamerunning=True
def printboard(board):
    print(board[0]+"|",board[1]+"|",board[2]+"|")
    print("__________")
    print(board[3]+"|",board[4]+"|",board[5]+"|")
    print("_________")
    print(board[6]+"|",board[7]+"|",board[8]+"|")
    
def  playerInput(board):
     y=int(input("enter a number btwn 1-9"))
     if(y>=0 and y<=9 and board[y-1]=="-"):
        board[y-1]=currentplayer
        
        

def checkrows(baoard):
    global winner
    if(board[0]==board[1]==board[2] and board[1]!="-"):
        winner=board[0]
        return True
    elif(board[3]==board[4]==board[5] and board[4]!="-"):
        winner=board[3]
        return True
    elif(board[6]==board[7]==board[8] and board[6]!="-"):
        winner =board[6]
        return True
def columns(board):
    global winner
    if(board[0]==board[3]==board[6] and board[0]!="-"):
        winner=board[3]
        return True
    elif(board[1]==board[4]==board[7] and board[1]!="-"):
        winner=board[1]
        return True
    elif(board[2]==board[5]==board[8] and board[2]!="-"):
        winner=board[2]
        return True
def diagonal(board):
    global winner
    if(board[0]==board[4]==board[8] and board[0]!="-"):
        winner=board[0]
        return True
    elif(board[2]==board[4]==board[6] and board[2]!="-"):
        winner=board[2]
        return True
    
def checktie(board):
    if "-" not in board:
        printboard(board)
        print("it is tie")
        gamerunning=False
def checkwin():
    if(checkrows(board) or columns(board) or diagonal(board)):
        print(f"the winner is{winner}")
        
def switchplayer():
    global currentplayer
    if(currentplayer=="X"):
        currentplayer="0"
    else:
        currentplayer="X"
        
def computer(board):
    while (currentplayer=="0"):
        position=random.randint(0,8)
        if(board[position]=="-"):
            board[position]="0"
            switchplayer()

while(gamerunning):
    printboard(board)
    playerInput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
    
    
    
