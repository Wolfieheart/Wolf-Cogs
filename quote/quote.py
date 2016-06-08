import discord
from discord.ext import commands
from random import choice as randomchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaultQuotes = [
	"Thats why I love switch hitting, I like to be in control ~ Jan, from the Hypermine Dragon Fight - 21st May 2016",
	"Thank you for wwaking within our server today- That sounds wrong. That does not sound PG at all -Jandoncom 24/5/16",
	"EVERYONE RUN! GECKOR IS DRIVING A TRUCK AGAIN /o\ ~ N7DeltaForce 03/06/16",
	"Everyone wants a piece of this -Jandoncom 7/6/2016",
	"I Want Khip Kho's Heart! ~ Jandoncom 7/6/2016"]

class Quote:
	"""Quote System for Red-DiscordBot"""

	def __init__(self, bot):
		self.bot = bot
		self.quotes = fileIO("data/quote/quotes.json", "load")

	def save_quotes(self)
		fileIO("data/quote/quotes.json", 'save', self.quotes)

	@commands.group(pass_context=True, invoke_without_command=True)
	async def quote(self, ctx):
		"""Random Quote to be Drawn"""
		await self.bot.say("Quote: " + randomchoice(self.quotes) + " ")

	@quote.command()
	async def add(self, quote):
		"""Adds a Quote to the List"""
		if quote in self.quotes:
			await self.bot.say("That quote is already in the database!")
		else:
			self.quotes.append(quote)
			self.save_quotes()
			await self.bot.say("Quote: " + quote + " has been saved to the database!")

	@quote.command()
	@checks.mod_or_permissions(adminstrator=True)
	async def remove(self, quote):
		"""Removes a Quote from the list"""
		if quote not in self.quotes:
			await self.bot.say("That quote is already in the database!")
		else:
			self.quotes.remove(quote)
			self.save_quotes()
			await self.bot.say("Quote: " + quote + " has been removed from the database!")

def check_folder():
	if not os.path.exists("data/quotes"):
		print("Creating data/quotes")
		os.makedirs("data/quotes")

def check_files():
	fileName = "data/quotes/quote.json"
	if not fileIO(fileName, "check"):
		print("Creating Empty Quote.json File")
		print("Creation Complete! Enjoy your new Quote System ~ Wolfstorm")
		fileIO(fileName, "save", defaultQuotes)

def setup(bot):
	check_folder()
	check_file()
	QuoteSystem = Quote(bot)
	bot.add_cog(QuoteSystem)


