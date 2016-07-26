import discord
from discord.ext import commands

class LoL:
	"""Laugh at a user"""

	def __init__(self,bot):
		self.bot = bot

	@commands.group(pass_context=True, invoke_without_command=True)
	async def lol(self, ctx, *, user : discord.Member=None):
		"""Cause everyone likes to have a laugh with ChronoxiaBot"""
		if ctx.invoked_subcommand is None:
			if user.id == self.bot.user.id:
				user = ctx.message.author
				await self.bot.say("- throws a pie  @" + user.name + " then proceed to laugh at " + user.name + " -" )
				return
			msg = "- starts to laugh with @" + user.name + " -"
			await self.bot.say(msg)
		
def setup(bot):
	n = LoL(bot)
	bot.add_cog(n)