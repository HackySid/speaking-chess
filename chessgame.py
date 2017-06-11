from gtts import gTTS
from playsound import playsound
STOCKFISH_PATH = "C:\stockfish-8-win\Windows\stockfish_8_x64.exe"
def speak(text):
    print text
    try:
        text1 = text.split(' ')
        text1 = '_'.join(text1)
        playsound(text1 +'.mp3')
    except:
        tts = gTTS(text=text,lang='en')
        text = text.split(' ')
        text = '_'.join(text)
        tts.save(text +'.mp3')
        playsound(text +'.mp3')
from stockfishpy.stockfishpy import *
from chess import Board,Move

chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 2, 'Ponder': 'false'})
speak(chessEngine.uci())
speak(chessEngine.isready())
chessEngine.ucinewgame()
board = Board()
move_list = []
while True:
     speak('Enter Move')
     move = raw_input()
     while Move.from_uci(move) not in board.legal_moves:
         speak('illegal move')
         move = raw_input()
     move_list.append(move)
     board.push(Move.from_uci(move))
     chessEngine.setposition(move_list)
     aimove = chessEngine.bestmove()
     aimove = aimove['bestmove']
     board.push(Move.from_uci(aimove))
     move_list.append(aimove)
     speak(aimove)
     print board
     if board.is_stalemate():
         speak('stalemate')
         break
     if board.is_insufficient_material():
         speak('insufficient material')
         break
     if board.can_claim_threefold_repetition():
         speak('Three fold repetion can be claimed')
     if board.can_claim_fifty_moves():
         speak('Fifty Moves can be claimed')
     if board.can_claim_draw():
         speak('Draw can be claimed')
     if board.is_fivefold_repetition():
         speak('Fivefold repetition')
     if board.is_seventyfive_moves():
         speak('Seventy five moves can be claimed')
     if board.is_check():
         speak('checkmate')
     if board.is_game_over():
         speak('Game over')
         break
     
     
     
     
     
     
     
                     
        
