from discord.ext import commands
import discord
import mytoken


def setup(bot):
    bot.add_cog(FileFilter(bot=bot))


class FileFilter(commands.Cog):
    """Adds functionality to filter out sertant files based on their extention"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.accepted_extentions: List[str] = ['.png', '.jpeg', '.gif']

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content.lower() == 'hello there':
            await message.channel.send('General Kenobi')
        # Solution starts here -----------------
        for attachment in message.attachments:
            if all([not attachment.filename.endswith(extension) for extension in self.accepted_extentions]):
                await message.channel.send("You can't upload this file type")
                await message.delete()
        # Solution ends here -----------------


bot = commands.Bot(command_prefix='!')
setup(bot)
bot.run(mytoken.get_token())
