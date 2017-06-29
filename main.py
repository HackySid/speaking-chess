import chess
board = chess.Board()
import chess.uci as chessuci
from gtts import gTTS
from playsound import playsound
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
        playsound(text + '.mp3')
speak('Type the name of the engine')
name = raw_input()
engine = chessuci.popen_engine(name)
speak('Enter movetime in seconds')
movetime = raw_input()
speak('Will you play black or white or ai versus ai')
colour = raw_input('(w/b/a)?\n')

if colour.lower in ['a','ai','ai v/s ai']:
    while board.is_game_over() == False:
        speak('Enter name of second black chess engine')
        name_ = raw_input()
        engine_ = chessuci.popen_engine(name)
        bestmove,pondermove = engine.go(movetime=movetime)
        speak(str(bestmove))
        board.push(bestmove)
        bestmovei,pondermovei = engine.go(movetime=movetime)
        speak(str(bestmovei))
        board.push(bestmovei)  
    

if colour.lower() in ['w','white','hite','ite','te','whit','whi','wh']:
    while board.is_game_over() == False:
        speak('Enter Move')
        move = raw_input() 
        board.push_san(move)
        engine.position(board)
        bestmove,pondermove = engine.go(movetime=movetime)
        speak(str(bestmove))
        board.push(bestmove)
    speak('game over')

if colour.lower() in ['b','black','lack','ack','ck','blac','bla','bl']:
    while board.is_game_over() == False:
        engine.position(board)
        bestmove,pondermove = engine.go(movetime=movetime)
        speak(str(bestmove))
        board.push(bestmove)
        speak('Enter Move')
        move = raw_input()
        board.push_san(move)
    speak('game over')


