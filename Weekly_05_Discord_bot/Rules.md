# Discord Bot Challenge

Corresponding [Discord message](https://discordapp.com/channels/501090983539245061/680851798340272141/724653570410020914)

You are nervous stepping into our new Tech With Tim Building as you are applying for the interview
you head to the waiting room getting more and more nervous you hear your name being called out so you head into the room just to be met with our bot expert face to face (aka sylte).
He gave you one task and a week to complete it.

## Task

```python
from discord.ext import commands

def setup(bot):
    bot.add_cog(FileFilter(bot=bot))

class FileFilter(commands.Cog):
    """Adds functionality to filter out sertant files based on their extention"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.accepted_extentions: List[str] = []

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        ... # Add your code here.
```

Using this format, check if the message has any attachments, if the attachments file extension is not in our list of valid extension delete the message and let the user know you cant post files of that filetype.
(The real challenge here is reading documentation for most people)

A list of allowed file extensions is available as `self.accepted_extentions` as seen in the code

## Submission

Submit your solution using the format described above :arrow_up:

## Grading

Idk man Sylte is grading it so you better live up to his standards.
This is something that will be added to our TWT bot so make sure it works as intended :wink:

## P.S.

This challenge is a bit different in several aspects, hope you like it.
