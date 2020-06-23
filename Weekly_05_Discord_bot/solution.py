from discord.ext import commands
import discord
import mytoken


def setup(bot):
    bot.add_cog(FileFilter(bot=bot))


class FileFilter(commands.Cog):
    """Adds functionality to filter out sertant files based on their extention"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.accepted_extentions: List[str] = []

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content.lower() == 'hello there':
            await message.channel.send('General Kenobi')
        # Solution starts here -----------------
        # check if the user is not a staff member
        if message.author.id not in [511334601977888798, 541272748161499147, 511332506780434438, 580911082290282506]:
            # navigate trough every attachment in the message
            for attachment in message.attachments:
                # delete the message if any of the attachment's extension is not inside the authorized list, or if there are no accepted extensions (list is empty)
                if any([not attachment.filename.endswith(extension.lower()) for extension in self.accepted_extentions]) or self.accepted_extentions == []:
                    await message.channel.send("You can't upload this file type !", delete_after=10)
                    await message.delete()
                    break
        # Solution ends here -----------------


bot = commands.Bot(command_prefix='!')
setup(bot)
bot.run(mytoken.get_token())
