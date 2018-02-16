import sys
import markov
import chatter

num_players = sys.argv[1]



# GAME FUNCTIONS
def process_markov_player_files():
    characters = []
    for i in range(2, len(sys.argv)):
        newChar = generateMarkovCharacter(sys.argv[i])
        characters.append(newChar)
    return characters

def generateMarkovCharacter(textfilePath):
    markov_input_text = markov.read_file(textfilePath)
    candidates = markov.split_text_into_chunks(markov.get_candidates(markov_input_text))

    while True:
        beginning = markov.select_chunk(candidates)
        #yield beginning
        yield markov.chunk_seq(markov_input_text, beginning, 5, 12) + '.'

def processChatterbotRequests(names):
    bots = []
    n = int(sys.argv[1]) - len(sys.argv) + 2
    # ['Margret', 'Sheila', 'Mortimer', 'Oscar', 'Billiph', 'Joseffia']
    for i in range(0, n):
        print ('\nTraining ' + names[i])
        bots.append(chatter.initBot(names[i]))
    return bots



# PRINT FUNCTIONS
def print_title():
    print('\n\n' +
' ___    __   _  _  _  _  ___   ____   __   ___  __    ___       \n' +
'(  ,)  /  \\ ( )( )( \\( )(   \\ (_  _) (  ) (  ,)(  )  (  _)   \n' +
' )  \\ ( () ) )()(  )  (  ) ) )  )(   /__\\  ) ,\\ )(__  ) _)   \n' +
'(_)\\_) \\__/  \\__/ (_)\\_)(___/  (__) (_)(_)(___/(____)(___)\n\n')

def main():
    print_title()
    markovPlayers = process_markov_player_files()
    names = [ 'Judienne', 'MagentasMaggiesMemory','Elvyn', 'PeculiarPenny', '\'Tunia', 'Centrifuge',
    'V. C. Pipes', 'RobarackObotama', 'Vixen', 'Vestiges', 'Shangela', 'Brooose', 'Ver de Koons', 'RebeccawithnoZs', 'Talia', 'Grenda', 'Bwana', 'Fin', 'History\'s Greatest Nightmare', 'History\'s Greatest Daydream', 'Vestiges II', 'Reckoning', 'Oranges', 'FamiliarFolly', 'Quine', 'DareDebbie', 'Orman', 'FocusFrancisFocus', 'Tornado-Tuesdae', 'QuackAttack', 'Yelle', 'Merk', 'Phil', 'Grahnt', 'Gebius', 'TokyoTerry', 'Forcefield C. Davis', 'FerdinandoArmando', 'Betty', 'Veronica', 'Once', 'Twice', 'Feathers', 'Heathers', 'McSheathers', 'Daffodeliliah', 'Reece', 'Benjammin', 'JD', 'Death2AllHumanz']
    chatterPlayers = processChatterbotRequests(names)
    print('\nBots trained. And now...\n\n')

    # n bots
    convoHasBegun = False
    for _ in range(0,10):
        i = 0
        for bot in chatterPlayers:
            if (convoHasBegun==False):
                    line = bot.get_response(next(markovPlayers[0]))
                    convoHasBegun = True
            line = str(bot.get_response(line))
            print(names[i] + ': ' + line)
            i += 1


    # # 2 bots and a markov
    # for _ in range(0,20):
    #     markovLine = next(markovPlayers[0])
    #     line = str(chatterPlayers[1].get_response(markovLine))
    #     print( names[2] + ': ' + markovLine)
    #     print(names[0] + ': ' + line)
    #     line = str(chatterPlayers[0].get_response(line))
    #     print(names[1] + ': ' + line)

    # # 2 bots
    # line = chatterPlayers[1].get_response(next(markovPlayers[0]))
    # for _ in range(0,10):
    #     line = str(chatterPlayers[0].get_response(line))
    #     print(names[0] + ': ' + line)
    #     line = str(chatterPlayers[1].get_response(line))
    #     print(names[1] + ':  ' + line)

    # # single philosophising bot
    # line = str(chatterPlayers[0].get_response(next(markovPlayers[0])))
    # for _ in range(0,10):
    #     print('Margret: ' + line)
    #     line = str(chatterPlayers[0].get_response(line))


if __name__ == '__main__':
    main()
