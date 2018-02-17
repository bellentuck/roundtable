import sys
import markov
import chatter
from threading import Timer

num_players = sys.argv[1]



# GAME FUNCTIONS
def process_markov_player_files():
    characters = []
    for i in range(3, len(sys.argv)):
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
    n = int(sys.argv[1]) #- len(sys.argv) + 2
    forum = sys.argv[2]
    # ['Margret', 'Sheila', 'Mortimer', 'Oscar', 'Billiph', 'Joseffia']
    for i in range(0, n):
        print ('\nTraining ' + names[i])
        if (forum == 'greetings'):
            bots.append(chatter.initBot(names[i], ['greetings']))
        elif (forum == 'historians'):
            bots.append(chatter.initBot(names[i], ['history']))
        elif (forum == 'aesthetes'):
            bots.append(chatter.initBot(names[i], ['history', 'literature',
            'movies', 'psychology', 'trivia']))
        elif (forum == 'queen-bees'):
            bots.append(chatter.initBot(names[i], ['conversations', 'gossip',
            'greetings']))
        elif (forum == 'brenda'):
            bots.append(chatter.initBot(names[i], ['brenda']))
        else:
            print('hi')
            bots.append(chatter.initBot(names[i]))
    return bots


#     ai.yml Training: [####################] 100%
# botprofile.yml Training: [####################] 100%
# computers.yml Training: [####################] 100%
# conversations.yml Training: [####################] 100%
# emotion.yml Training: [####################] 100%
# food.yml Training: [####################] 100%
# gossip.yml Training: [####################] 100%
# greetings.yml Training: [####################] 100%
# history.yml Training: [####################] 100%
# humor.yml Training: [####################] 100%
# literature.yml Training: [####################] 100%
# money.yml Training: [####################] 100%
# movies.yml Training: [####################] 100%
# politics.yml Training: [####################] 100%
# psychology.yml Training: [####################] 100%
# science.yml Training: [####################] 100%
# sports.yml Training: [####################] 100%
# trivia.yml Training: [####################] 100%



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
    print('\nGreat. We\'re trained. Now...\n\n')

    # Start the convo,
    # time = input('How many seconds would you like our discussion to last?  ')
    # if (time == '' or type(float(time)) == 'NaN'):
    #     time = 10
    # then time and when we're at time stop
    # get a topic (or have it via Markov model if that's there)
    topic = input('Start us off with a topic?  ')
    if (topic == ''):
        topic = next(markovPlayers[0])


    # def endConvo(hasConvoEndedVar):
    #     hasConvoEndedVar[0] = True
    #     return hasConvoEndedVar[0]

    def detectLoops(a, b, c, d):
        if (a == b and b == c and c == d):
            return True
        if (a == c and b == d):
            return True
        return False

    convoHasBegun = False
    convoHasEnded = False
    line = ''
    prevLine = ''
    prevPrevLine = ''
    prevPrevPrevLine = ''
    # t = Timer(int(time), endConvo, [convoHasEnded])
    # t.start()
    while (convoHasEnded==False):
        i = 0
        for bot in chatterPlayers:
            if (convoHasEnded==True):
                break
            if (convoHasBegun==False):
                line = bot.get_response(topic)
                convoHasBegun = True
            elif (line[-1] == '?'):
                line = input('\nYou: ')

            prevPrevPrevLine = prevPrevLine
            prevPrevLine = prevLine
            prevLine = line
            line = str(bot.get_response(line))

            isLoop = detectLoops(line, prevLine, prevPrevLine, prevPrevPrevLine)

            if (isLoop == True):
                line = input('\nYou: ')
                line = str(bot.get_response(line))

            print('\n' + names[i] + ': ' + line)
            i += 1



    # # n bots
    # convoHasBegun = False
    # for _ in range(0,10):
    #     i = 0
    #     for bot in chatterPlayers:
    #         if (convoHasBegun==False):
    #                 line = bot.get_response(topic)
    #                 convoHasBegun = True
    #         line = str(bot.get_response(line))
    #         print(names[i] + ': ' + line)
    #         i += 1


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


# option to respond
# option to set topic if not having markov




# Judienne: what is government

# MagentasMaggiesMemory: an established system of political administration by which a nation, state, district, etc. is governed.

# Elvyn: tell me what you know about gossips

# PeculiarPenny: Jordan said he notice that lots of other people are talking to me how many.

# Judienne: Gossips about kevin

# MagentasMaggiesMemory: Kevin said he then asked his mother why she was keeping napkins in the bathroom.

# Elvyn: Gossips about kevin
