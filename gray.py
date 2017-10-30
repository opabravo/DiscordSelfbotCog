from discord.ext import commands
from random import randint
import random
import discord

class Gray:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="check")
    async def check(self, ctx, text):
        """Checks A Link""" 
        msg = '```diff\n+ Result : ```'+'https://spoopy.link/' + str(text)
        await ctx.message.delete()
        if len(msg) > 2000:
            await ctx.send('Link Too Long')
        else:
            await ctx.send(msg)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.Member=None):
        """Hug your waifu!"""
        author = ctx.message.author.mention

        hug = "**{} gave {} a hug!**"
        hugself= "**{} Hugs himself TT**"
        
        choices = ['http://i.imgur.com/sW3RvRN.gif', 'http://i.imgur.com/gdE2w1x.gif', 'http://i.imgur.com/zpbtWVE.gif', 'http://i.imgur.com/ZQivdm1.gif', 'http://i.imgur.com/MWZUMNX.gif', 'https://i.imgur.com/8futZnQ.gif' ,'https://i.imgur.com/viWWVub.gif', 'http://imgur.com/a/N7F1C', 'https://i.imgur.com/mXGKeyN.gif' ,'https://i.imgur.com/mxaqyUu.gif', 'https://i.imgur.com/dLUetXa.gif', 'https://i.imgur.com/hM1LcZf.gif']
        
        image = random.choice(choices)
        
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=hug.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=hugself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def kiss(self, ctx, member: discord.Member=None):
        """Kiss your waifu!"""
        
        author = ctx.message.author.mention
        
        kiss = "**{0} gave {1} a kiss!**"
        kissself= "**{} Kissed himself :kiss: **"
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'https://i.imgur.com/4VePCc4.gif', 'http://i.imgur.com/3wv088f.gif', 'https://i.imgur.com/dG73Bmb.gif', '', 'https://i.imgur.com/5epo3Ls.gifv', 'https://i.imgur.com/5Hx4D9n.gif', 'https://i.imgur.com/j9Gvrrd.gif', 'https://i.imgur.com/jEmrZGS.gif', 'https://i.imgur.com/kn9awse.gif', 'https://i.imgur.com/AIJn1LF.mp4' 'https://i.imgur.com/uoaOqXO.gif', 'https://i.imgur.com/dJWlgnr.gif', 'https://i.imgur.com/G8Mbg1Z.gif', 'https://i.imgur.com/evjODur.gif', 'https://i.imgur.com/tumv7DY.gif', 'https://i.imgur.com/JZLaOA2.gifv']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=kiss.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=kissself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def lick(self, ctx, member: discord.Member=None):
        """Lick your waifu!"""
        author = ctx.message.author.mention
        
        lick = "**{0} licked {1}!**"
        lickself="{} licked himself :thinking: "
        
        choices = ['https://images-ext-2.discordapp.net/external/EVS-yozpRCwqM9JrkkgoTry1IqkDyTJVNjF7ZhIik5U/https/cdn.weeb.sh/images/S1Ill0_vW.gif', 'https://images-ext-2.discordapp.net/external/QAh4YL0JFxeg7wWxw4G3cCucyPRj2fHB3w3zmONGtjg/https/cdn.weeb.sh/images/Bkxge0uPW.gif', 'https://images-ext-2.discordapp.net/external/9xiregisvDewxtEC9iCJPqJWNlrFEn3kcj3YA-ev_Po/https/cdn.weeb.sh/images/H1EJxR_vZ.gif', 'https://images-ext-2.discordapp.net/external/9bHT8aeSTZnMcfTFsR4S_IawF7WOUwK4fKLGhIHVYnw/https/cdn.weeb.sh/images/Syg8gx0OP-.gif', 'https://images-ext-1.discordapp.net/external/1AoFzXaNiKcnBc4OrS3R7jsf9MJEDcikx38nUkbFQW8/https/cdn.weeb.sh/images/HJRRyAuP-.gif', 'https://images-ext-2.discordapp.net/external/j_SDM7t05yLMhzcgBn_omAVg0RbMRpSaK4m_YzTzvuU/https/cdn.weeb.sh/images/HJ2ggROPZ.gif', 'https://images-ext-2.discordapp.net/external/Q1_n8vJ0MNURUGkRTYneZQ17_zzG1Jtw9ixyHyOecQY/https/cdn.weeb.sh/images/S17kgRuP-.gif', 'https://images-ext-1.discordapp.net/external/thImffzNHXbD4uB3R-av9x0cvsdmumPWfN8IW7huw1c/https/cdn.weeb.sh/images/Bkagl0uvb.gif', 'http://data.whicdn.com/images/137509075/original.gif', 'http://i0.kym-cdn.com/photos/images/newsfeed/001/145/832/ed1.gif', 'http://i.imgur.com/jMSv255.gif', 'http://pa1.narvii.com/5934/f8f511890cb7372160b907fbaf4cbcd9fb32f91b_hq.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=lick.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=lickself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def pat(self, ctx, member: discord.Member=None):
        """Pat your senpai/waifu!"""
        author = ctx.message.author.mention
        
        pat = "**{0} got patted by {1}!**"
        patself="{} patted himelf :hugging: "
        
        choices = ['http://i.imgur.com/10VrpFZ.gif', 'http://i.imgur.com/x0u35IU.gif', 'http://i.imgur.com/0gTbTNR.gif', 'http://i.imgur.com/hlLCiAt.gif', 'http://i.imgur.com/sAANBDj.gif', 'https://i.imgur.com/wtxwpm1.mp4', 'https://i.imgur.com/rQdg0Xr.gif', 'https://i.imgur.com/3eR7weH.gif', 'https://i.imgur.com/cK8Ro3x.gif', 'https://i.imgur.com/g1H0dHv.gif', 'https://i.imgur.com/qtHlt3n.gif', 'https://i.imgur.com/K3fad03.gif', 'https://i.imgur.com/bzzodCZ.mp4', 'https://i.imgur.com/usxXmP0.gif', 'https://i.imgur.com/mLyG5LV.gif', 'https://i.imgur.com/sIOXrRK.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=pat.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=patself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def slap(self, ctx, member: discord.Member=None):
        """Slap your senpai/waifu!"""     
        author = ctx.message.author.mention
        
        slap = "**{0} got slapped by {1}**"
        slapself = "**{} slapped himelf**"
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'https://i.imgur.com/4VePCc4.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif', 'https://i.imgur.com/5epo3Ls.gifv', 'https://i.imgur.com/5Hx4D9n.gif', 'https://i.imgur.com/j9Gvrrd.gif']
        
        image = random.choice(choices)
        
        if member:
            mention = member.mention
            embed = discord.Embed(description=slap.format(author, mention), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
            
        else:
            embed = discord.Embed(description=slapself.format(author), color=discord.Colour.from_rgb(r=randint(0, 255), g=randint(0, 255), b=randint(0, 255)))
        
        embed.set_image(url=image)
        await ctx.send(embed=embed)

            
        
def setup(bot):
    bot.add_cog(Gray(bot))
