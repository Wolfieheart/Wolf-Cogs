import discord
from discord.ext import commands
import time 
from __main__ import send_cmd_help

class Ping:
	"""Ping"""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(pass_context=True)
	async def pingit(self, ctx):
		"""Ping Timer"""
		channel = ctx.message.channel
		timer1 = time.perf_counter()
		await self.bot.send_typing(channel)
		timer2 = time.perf_counter()
		await self.bot.say("Pong: {}ms".format((timer2-timer1)*1000))

def setup(bot):
	bot.add_cog(Ping(bot))
