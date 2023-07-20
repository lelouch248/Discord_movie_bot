import discord


def get_help_data():
    embed = discord.Embed(title="Bot Help", description="Here are the available commands:", color=0x4b7bec)

    embed.add_field(name="!!movie <movie name>", value="Get information about a movie", inline=False)
    embed.add_field(name="!!ts <tv show name>", value="Get information about a TV show", inline=False)
    embed.add_field(name="!!anime <anime name>", value="Get information about an anime", inline=False)
    embed.add_field(name="!!random anime", value="Generates a random anime", inline=False)

    return embed
