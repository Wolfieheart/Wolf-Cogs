import discord
from discord.ext import commands
from random import choice as randomchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaults = [ 
	"A Pillow",
	"A Slice of Pizza",
	"999 Pokéballs for Pokémon Go!",
	"A Mountain of Sand",
	"A Tight, Warm, Gentle Hug",
	"A Stack of Sea Lanterns",
	"A Nice, Warm Cup of Coffee",
	"A Roasted Marshmallow Smore",
	"A Nice, Warm Cup of Tea",
	"A Picnic @BasketMC#6501"
	]

class Give:
	"""Give: Does as it says on the tin! Give the user something!"""

	def __init__(self, bot):
		self.bot = bot
		self.items = fileIO("data/give/items.json", "load")

	def save_items(self):
		fileIO("data/give/items.json", 'save', self.items)

	@commands.group(pass_context=True, invoke_without_command=True)
	async def give(self, ctx, *, user : discord.Member=None):
		if ctx.invoked_subcommand is None:
			if user.id == self.bot.user.id:
				user = ctx.message.author
				await self.bot.say("- gives " + user.name +" a shovel and says 'Go clear that mountain for @Jan#7096'" )
				return
			await self.bot.say("- gives " + randomchoice(self.items) + " to " + user.name + "! Have fun :D -")

	@give.command()
	@checks.mod_or_permissions(administrator=True)
	async def add(self, giveitem):
		if giveitem in self.items:
			await self.bot.say("Awww! That is already in the list of items that can be given to people! Sowwie :crying_cat_face:")
		else:
			self.items.append(giveitem)
			self.save_items()
			await self.bot.say("YAY! I have a new item to give people! Thank you" + user.name + ":smile_cat: !")


	@give.command()
	@checks.mod_or_permissions(administrator=True)
	async def remove(self, giveitem):
		if giveitem not in self.items:
			await self.bot.say("Awww! That is already in the list of items that can be given to people! Sowwie :crying_cat_face:")
		else:
			self.items.remove(giveitem)
			self.save_items()
			await self.bot.say(" *starts crying* I'm sad to see that item g-g-g-go! :crying_cat_face:")

def folder_check():
	if not os.path.exists("data/give"):
		print("Creating Folders")
		os.makedirs("data/give")
		print("Folder Structure Created!")

def file_check():
	file = "data/give/items.json"
	if not fileIO(file, "check"):
		print("Creating Item List")
		fileIO(file, "save", defaults)
		print ("File Creation Complete!")

def setup(bot):
	folder_check()
	file_check()
	give = Give(bot)
	bot.add_cog(give)