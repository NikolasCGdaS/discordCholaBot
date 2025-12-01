import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

<<<<<<< HEAD
class CholaBot(commands.Bot):
    def __init__(self):
        load_dotenv()
        self.botToken = os.getenv('DISCORD_TOKEN')

        logDeExecucao = logging.FileHandler(
            filename='discordBot.log', encoding='utf-8', mode='w'
        )

=======
logger = logging.getLogger(__name__)

class CholaBot(commands.Bot):
    def __init__(self, log_handler):

        # Define as funcionalidades a serem carregadas
        self.cogsToLoad = [
            'modules.basicCommands.basicService',
            'modules.frequencyChecker.FrequencyControl',
            'modules.music.musiccontroller'
        ]

        # Carrega o arquivo .env e lê o token do bot dentro dele
        load_dotenv()
        self.botToken = os.getenv('DISCORD_TOKEN')

        # Declara os intents
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix='cb/',
            intents=intents,
<<<<<<< HEAD
            log_handler=logDeExecucao,
            log_level=logging.DEBUG
        )

    async def setup_hook(self):
        # Carrega o módulo musiccontroller
        await self.load_extension("modules.music.musiccontroller")
        print("Setup concluído.")
=======
            log_handler=log_handler,
            log_level=logging.DEBUG
        )

    # Carrega as Cogs especificadas anteriormente
    async def setup_hook(self):
        for cogName in self.cogsToLoad:
            try:
                await self.load_extension(cogName)
                print(f"Cog '{cogName}' loaded")
            except commands.ExtensionNotFound:
                print(f"Erro: Cog '{cogName}' não foi encontrado.")
            except Exception as e:
                print(f"Falha ao carregar Cog '{cogName}': {type(e).__name__}: {e}")
                logger.error(f"Falha ao carregar Cog '{cogName}': {e}", exc_info=True)
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f

    async def on_ready(self):
        print(f"{self.user.name} ativo e operante!")
        canal = self.get_channel(962854221244411964)
        if canal:
            await canal.send("Estou ativo")

<<<<<<< HEAD
    async def on_member_join(self, member):
        await member.send(f"Bem vindo {member.name}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "cholabot" in message.content.lower() and "ola" in message.content.lower():
            await message.channel.send(f"Ola {message.author.mention} !!!")

        await self.process_commands(message)

    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            canal = self.get_channel(962854221244411964)
            if canal:
                await canal.send(
                    f"{member.name} entrou em {after.channel}"
                )

    def iniciar(self):
        self.run(self.botToken)
=======
    def iniciar(self):
        self.run(self.botToken)
        
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f
