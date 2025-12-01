from chatbot import CholaBot
<<<<<<< HEAD

if __name__ == "__main__":
    bot = CholaBot()
=======
import logging
import os

# Define o arquivo que trará os logs de execução
logDeExecucao = logging.FileHandler(
    filename='discordBot.log', encoding='utf-8', mode='w'
)

logging.basicConfig(
    handlers=[logDeExecucao],
    level=logging.DEBUG
)

if __name__ == "__main__":
    bot = CholaBot(log_handler=logDeExecucao)
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f
    bot.iniciar()
