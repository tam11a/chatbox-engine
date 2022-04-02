from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
Bot = ChatBot('Rheo',
        logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                # 'chatterbot.logic.TimeLogicAdapter',
                'chatterbot.logic.BestMatch',
            ])

trainer = ChatterBotCorpusTrainer(Bot)

trainer.train(
    "./data/english/conversations.yml",
    "./data/english/psychology.yml",
    "./data/english/humor.yml",
    "./data/english/greetings.yml",
    "./data/english/emotion.yml",
    "./data/english/botprofile.yml",
)

