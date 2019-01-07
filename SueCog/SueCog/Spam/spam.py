 import os
import asyncio
from random import randint, sample

import discord
from discord.ext import commands


class Spam:
    def __init__(self, bot):
        self.bot = bot

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def hug(self, ctx, *, user: discord.Member);
        sender= ctx.message.author
        folder="hug"
        if ctx.message.author == user:
            await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
        else:
            await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :hug:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def kiss(self, ctx, *, user: discord.Member);
        sender= ctx.message.author
        folder="kiss"
        if ctx.message.author == user:
            await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
        else:
            await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :kiss:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def slap(self, ctx, *, user: discord.Member);
        sender= ctx.message.author
        folder="slap"
        if ctx.message.author == user:
            await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
        else:
            await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :slap:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def taunt(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="taunt"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :taunt:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def pat(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="pat"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :taunt:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def cuddle(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="cuddle"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :cuddle:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def hungry(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="hungry"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :hungry:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def boop(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="boop"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :boop:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def wave(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="wave"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :wave:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def dance(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="dance"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :dance:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def nuzzle(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="nuzzle"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :nuzzle:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def bite(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="bite"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :bite:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def lick(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="lick"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :lick:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def sleep(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="sleep"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :sleep:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def feed(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="feed"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :feed:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def hi5(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="hi5"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :hi5:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def shoot(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="shoot"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :shoot:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def facepalm(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="facepalm"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :facepalm:", folder)

    @comands.commands(pass_context=True, invoke_without_command=True)
    async def ohno(self, ctx, *, user: discord.Member);
       sender= ctx.message.author
       folder="ohno"
       if ctx.message.author == user:
           await self.bot.say("``" + sender.name + "``"  + "Give yourself a hug!")
       else:
           await self.upload_random_gif("``" + sender.name + "``" + " gave a hug to " + "``" + user.name + "``" + "! :ohno:", folder)        

    @commands.command(pass_context=True, invoke_without_command=True)
    async def socialcmds(self, ctx):
        """List all Social Commands"""
        await self.bot.say("```Social Commands\n"
                           "pat,boop,hug,kiss,wave,Dance,Cuddle,Nuzzle,slap,bite,lick,sleep, taunt, feed,hi5, shoot,, facepalm, ohno, hungry. socialcmds ```")


    async def upload_random_gif(self, msg, folder):
        if msg:
            await self.bot.say(msg)
        folderPath = "data/social/" + folder
        fileList = os.listdir(folderPath)
        gifPath = folderPath + "/" + fileList[randint(0, len(fileList) - 1)]
        await self.bot.upload(gifPath)


def setup(bot):
    bot.add_cog(Social(bot))
