import discord
from random import randint
from discord.ext import commands

'''Turn every message into image, modified from Appu's Allembeds cog'''


class AllImg:

    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        
    @commands.command(pass_context=True, aliases=["allimg", "tgi"])
    async def toggleimg(self, ctx):
        """Turns every message into image"""
        self.enabled = not self.enabled
        await ctx.send(self.bot.bot_prefix + "Successfully toggled turning all messages to embeds to `{}`!".format(self.enabled))
        
    async def on_message(self, message):
        if message.author == self.bot.user:
            if not message.embeds and self.enabled:
                image = "https://dummyimage.com/1280x480/36393E/ffffff.png&text={}".format(message.content)
                #await message.delete()
                embed = discord.Embed(color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
                embed.set_image(url=image)
                await message.edit(embed=embed)



def setup(bot):
    bot.add_cog(AllImg(bot))
