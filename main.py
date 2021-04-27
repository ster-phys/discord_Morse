#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import config
from Morse import Morse

# generate wav
import genToneSource

# Get TOKEN
TOKEN = config.DISCORD_TOKEN

# Bot setting
commandPrefix = '?'
bot = commands.Bot(command_prefix=commandPrefix)
bot.remove_command("help")

# Operation at startup
@bot.event
async def on_ready():
    print("Logged in as {} ({})".format(bot.user.name,bot.user.id))

# Ignore commands from bots
@bot.event
async def from_bot(ctx):
    if ctx.author.bot:
        return

@bot.group()
async def morse(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid morse command passed...")

@morse.command()
async def join(ctx,*,arg=""):
    # User must be on the voice channel to use the command
    if not ctx.author.voice:
        await ctx.send("You need to connect to the voice channel.")
        return
    # already connected
    if ctx.guild.voice_client:
        await ctx.send("Already connected.")
        return
    # connect
    await ctx.author.voice.channel.connect()
    await ctx.send("Successfully connected.")

@morse.command()
async def leave(ctx,*,arg=""):
    # check connection
    if not ctx.guild.voice_client:
        await ctx.send("There is no connection.")
        return
    # disconnect
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Successfully disconnected.")

@morse.command()
async def send(ctx,*,arg=""):
    if not ctx.guild.voice_client:
        await ctx.send("You need to connect me first.")
        await ctx.send("Execute: `?morse join`")
        return
    await Morse.Morse(ctx,arg).main()

bot.run(TOKEN)
