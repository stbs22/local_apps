#This should be at your other imports at the top of your code
import asyncio

async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
    roleobject = discord.utils.get(ctx.message.guild.roles, id=730016083871793163)
    await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
    await user.add_roles(roleobject)
    if unit == "s":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m":
        wait = 60 * duration
        await asyncio.sleep(wait)
    await user.remove_roles(roleobject)
    await ctx.send(f":white_check_mark: {user} was unmuted")   
