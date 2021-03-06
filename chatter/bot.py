from chatterbot import ChatBot

def initBot(name='', corpora=['all']):
    chatbot = ChatBot(
        name,
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )
    if (corpora[0] == 'all'):
        print(corpora)
        chatbot.train("chatterbot.corpus.english")
    elif (corpora[0] == 'brenda'):
        chatbot.train('/Users/ben/Documents/pyGame/roundtable/chatter/brenda.yml')
    else:
        for i in range(0, len(corpora)):
            chatbot.train("chatterbot.corpus.english." + corpora[i])
    # # Train based on the english corpus
    # chatbot.train("chatterbot.corpus.english")

    # # Train based on english greetings corpus
    # chatbot.train("chatterbot.corpus.english.greetings")

    # # Train based on the english conversations corpus
    # chatbot.train("chatterbot.corpus.english.conversations")

    #chatbot.train("chatterbot.corpus.english.food")
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

    return chatbot

