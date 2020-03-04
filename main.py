# Libs
import discord # For discord
from discord.ext import commands # For discord
import logging # For logging


# Defining a few things
bot = commands.Bot(command_prefix='-', case_insensitive=True)
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    # Another way to use variables in strings
    print("-----\nLogged in as: {} : {}\n-----\nMy current prefix is: -\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Chilling !"))

@bot.command(name='hi', aliases=['hello'])
async def hi(ctx):
    """
    A simple command which says hi to the author.
    """
    await ctx.send(f"Hi {ctx.author.mention}!")
    # Another way to do this code is (user object).mention
    #await ctx.send(f"Hi <@{ctx.author.id}>!")

@bot.command()
async def echo(ctx, *, message=None):
    """
    A simple command that repeats the users input back to them.
    """
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    """
    A simple command to get ping of the bot.
    
    """
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is {ping}ms")

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")


@bot.command()
async def prefix(ctx):
    """
    A simple command to get prefix of the bot
    
    """
    prefix = bot.command_prefix
    await ctx.channel.send(f"The prefix is : {prefix}")

@bot.command()
async def setprefix(ctx, *, new_prefix=None ):
    """
    A simple command to get prefix of the bot
    
    """
    newprefix = new_prefix or "Please provide the new prefix."
    bot.command_prefix = newprefix
    await ctx.channel.send(f"The new prefix is : {newprefix}")
    
@bot.command()
async def clear(ctx, *, number=None):
    """
    A simple command that repeats the users input back to them.
    """
    number = int(number) or "Please provide the number of messages to be deleted."
    for x in range(number):
        await ctx.message.delete()
        
    await ctx.channel.send(f"{number} messages were deleted")

bot.run('Njc3ODkzMjM1Mzg1MDQwOTM2.Xl66Uw._59Mopd4II_zG4p4A-GiYK5hVeM') # Runs our bot