import eel
import time
eel.init('web')

# variable for keep victory score player state
countVictoryP1 = 0
countVicotryP2 = 0
Tie = 0
roundVictoryP1 = False
roundVictoryP2 = False

isLoad = False
topScore = []
historyMatch = []
roundPlay = 0

startMatch = 0
endMatch = 0

#variable for keep pattern to win board game(3x3)
winBoardPattern3 = [[1,2,3],[5,6,7],[9,10,11],[1,5,9],[2,6,10],[3,7,11],[1,6,11],[9,6,3]]
#variable for keep pattern to win board game(4x4)
winBoardPattern4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16],[1,6,11,16],[4,7,10,13]]


@eel.expose
def Answer(p1,p2,size):
    global winBoardPattern3
    global winBoardPattern4
    global countVictoryP1
    global countVicotryP2
    global roundVictoryP1
    global roundVictoryP2
    global Tie
    global isLoad
    global roundPlay
    global endMatch
    global startMatch
    maxSelectX = 0
    maxSelectO = 0
    boardPattern = []

    #variable for check opportunity to win this match 
    p1Board = []
    p2Board = []

    #variable for check round win 
    roundVictoryP1 = False
    roundVictoryP2 = False

    isLoad = False
    if(size == 3 ):
        boardPattern = winBoardPattern3
        maxSelectX = 5
        maxSelectO = 4
    if(size == 4):
        boardPattern = winBoardPattern4
        maxSelectX = 8
        maxSelectO = 8
        
    for pattern in boardPattern:
        p1Board = (set(pattern) - set(p1)) 
        p2Board = (set(pattern) - set(p2)) 
        if(len(p1Board) == 0):
            print("Player 1 victory")
            countVictoryP1 +=1 
            roundPlay +=1
            roundVictoryP1 = True
            roundVictoryP2 = False
            endMatch = time.time()
            durationMatch = round((endMatch - startMatch),2)
            historyMatch.append([0,durationMatch,size])
            print("duration match: {}".format(durationMatch))
            return (countVictoryP1,countVicotryP2,roundVictoryP1,roundVictoryP2,Tie,isLoad)
        if(len(p2Board) == 0):
            print("Player 2 victory")
            countVicotryP2 += 1
            roundPlay +=1
            roundVictoryP2 = True
            roundVictoryP1 = False
            endMatch = time.time()
            durationMatch = round((endMatch - startMatch),2)
            historyMatch.append([1,durationMatch,size])
            print("duration match: {}".format(endMatch - startMatch))
            return(countVictoryP1,countVicotryP2,roundVictoryP1,roundVictoryP2,Tie,isLoad)
    if(len(p1) == maxSelectX and len(p2) == maxSelectO and len(p1Board) != 0 and len(p2Board) != 0):
        Tie += 1
        roundPlay += 1
        endMatch = time.time()
        durationMatch = round((endMatch - startMatch),2)
        historyMatch.append([2,durationMatch,size])
        print("duration match: {}".format(durationMatch))
        return(countVictoryP1,countVicotryP2,roundVictoryP1,roundVictoryP2,Tie)
        print("draw")

@eel.expose
def getScore():
    global isLoad
    global startMatch
    startMatch = time.time()
    isLoad = True
    return(countVictoryP1,countVicotryP2,roundVictoryP1,roundVictoryP2,Tie,isLoad)

@eel.expose
def getHistory():
    return(historyMatch)

@eel.expose
def getTopScore():
    topScore = []
    if(countVictoryP1 > countVicotryP2):
        topScore=[[0,countVictoryP1,Tie,roundPlay],[1,countVicotryP2,Tie,roundPlay]]
        return(topScore)
    if(countVicotryP2 > countVictoryP1):
        topScore=[[1,countVicotryP2,Tie,roundPlay],[0,countVictoryP1,Tie,roundPlay]]
        return(topScore)
    if(countVictoryP1 == countVicotryP2):
        topScore=[[1,countVicotryP2,Tie,roundPlay],[0,countVictoryP1,Tie,roundPlay]]
        return(topScore)

eel.start('home.html', size=(980, 980))    # Start
