import discord
from discord.ext import commands
from random import choice as randomchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaults = [
	"Gohadouken",
	"Zanku Hadouken",
	"Shakunetsu Hadouken",
	"Gorai Hadouken",
	"Metsu Hadouken",
	"Messatsu Gou Hadou",
	"Tenma Go Zankuu",
	"Meido Gohado",
	"Denjin Hadouken",
	"Ren Hadouken",
	"Baku Hadouken",
	"Gadouken"]

class Hadoken:
	"""Hadoken: Street Fighters Version of !slap

	Credit to the Maker of !slap for giving me a hand with the Random
	Choice Selection. Also credit to @SolidX on #ThePillowFort for 
	giving me the Idea of making this cog a thing"""

	def __init__(self, bot):
		self.bot = bot
		self.fists = fileIO("data/hadoken/fists.json", "load")

	def save_fists(self):
		fileIO("data/hadoken/fists.json", 'save', self.fists)

	@commands.group(pass_context=True, invoke_without_command=True)
	async def hadoken(self, ctx, *, user : discord.Member=None):
		"""Do the Hadoken on a user"""
		if ctx.invoked_subcommand is None:
			if user.id == self.bot.user.id:
				user = ctx.message.author
				await self.bot.say("- uses " + randomchoice(self.fists) + " on " + user.name + " - \n\n Next Time " + user.name + " Dont Hadoken Me! :crying_cat_face:" )
				return
			await self.bot.say("- uses " + randomchoice(self.fists) + " on " + user.name + " -")

	@hadoken.command()
	async def add(self, fist):
		"""Adds a Fist to the List"""
		if fist in self.fists:
			await self.bot.say("That fist is already on our list")
		else:
			self.fists.append(fist)
			self.save_fists()
			await self.bot.say("Congrats, your new fist has been added to the list! :D")

	@hadoken.command()
	@checks.is_owner()
	async def remove(self, fist):
		"""Remove a Fist from the list"""
		if fist not in self.fists:
			await self.bot.say("That fist is already on our list")
		else:
			self.fists.remove(fist)
			self.save_fists()
			await self.bot.say("Awww! Im sad to see that Item Removed :(  *sigh*") 

def folder_check():
	if not os.path.exists("data/hadoken"):
		print("Creating data/hadoken :D")
		os.makedirs("data/hadoken")


def file_check():
	file = "data/hadoken/fists.json"
	if not fileIO(file, "check"):
		print("Creating Empty Fists.json File")
		print("Creation Complete! Enjoy !hadoken ~ Wolfstorm")
		fileIO(file, "save", defaults)

def setup(bot):
	folder_check()
	file_check()
	FistsOfFury = Hadoken(bot)
	bot.add_cog(FistsOfFury)
