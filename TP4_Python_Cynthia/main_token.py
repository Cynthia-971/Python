import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")

doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN"))