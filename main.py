from Board import Board
from InputParser import InputParser
from AI import AI
import sys
import random
import pyttsx3

WHITE = True
BLACK = False
engine = pyttsx3.init()

def speak(input):
    print(input)
    engine.say(input)

def askForPlayerSide():
    playerChoiceInput = input('w or b? ').lower()
    engine.say("What side would you like to play as?")
    if 'w' in playerChoiceInput:
        print("You will play as white")
        return WHITE
    else:
        print("You will play as black")
        return BLACK


def askForDepthOfAI():
    depthInput = 2
    try:
        engine.say("How deep should the AI look for moves?")
        depthInput = int(input("How deep should the AI look for moves?\n"
                               "Warning : values above 3 will be very slow."
                               " [n]? "))
    except:
        speak("Invalid input, defaulting to 2")
    return depthInput


def printCommandOptions():
    undoOption = 'u : undo last move'
    printLegalMovesOption = 'l : show all legal moves'
    randomMoveOption = 'r : make a random move'
    quitOption = 'quit : resign'
    moveOption = 'a3, Nc3, Qxa2, etc : make the move'
    options = [undoOption, printLegalMovesOption, randomMoveOption,
               quitOption, moveOption, '', ]
    print('\n'.join(options))


def printAllLegalMoves(board, parser):
    for move in parser.getLegalMovesWithShortNotation(board.currentSide):
        speak(move.notation)


def getRandomMove(board, parser):
    legalMoves = board.getAllMovesLegal(board.currentSide)
    randomMove = random.choice(legalMoves)
    randomMove.notation = parser.notationForMove(randomMove)
    return randomMove


def makeMove(move, board):
    print()
    speak("Making move : " + move.notation)
    board.makeMove(move)


def printPointAdvantage(board):
    speak("Currently, the point difference is : " +
          str(board.getPointAdvantageOfSide(board.currentSide)))


def undoLastTwoMoves(board):
    if len(board.history) >= 2:
        board.undoLastMove()
        board.undoLastMove()


def startGame(board, playerSide, ai):
    parser = InputParser(board, playerSide)
    while True:
        print(board)
        print()
        if board.isCheckmate():
            if board.currentSide == playerSide:
                speak("Checkmate, you lost")
            else:
                speak("Checkmate! You won!")
            return

        if board.isStalemate():
            if board.currentSide == playerSide:
                speak("Stalemate")
            else:
                speak("Stalemate")
            return

        if board.currentSide == playerSide:
            # printPointAdvantage(board)
            move = None
            speak("It's your move.")
            speak(" Type '?' for options ? ")
            command = input().lower()
            if command == 'u':
                undoLastTwoMoves(board)
                continue
            elif command == '?':
                printCommandOptions()
                continue
            elif command == 'l':
                printAllLegalMoves(board, parser)
                continue
            elif command == 'r':
                move = getRandomMove(board, parser)
            elif command == 'quit':
                return
            else:
                move = parser.moveForShortNotation(command)
            if move:
                makeMove(move, board)
            else:
                speak("Couldn't parse input, enter a valid command or move.")

        else:
            speak("AI thinking...")
            move = ai.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)

board = Board()
playerSide = askForPlayerSide()
print()
aiDepth = askForDepthOfAI()
opponentAI = AI(board, not playerSide, aiDepth)

try:
    startGame(board, playerSide, opponentAI)
except KeyboardInterrupt:
    sys.exit()
