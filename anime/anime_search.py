import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()


def get_anime_data(query):
    print("inside anime data")
    url = f"https://api.jikan.moe/v4/anime?q={query}"
    response = requests.get(url)
    data = response.json()["data"][0]

    if data:
        title = data["title"]
        synopsis = data["synopsis"]
        image_url = data["images"]["jpg"]["small_image_url"]
        trailer_url = data["trailer"]["url"]
        anime_type = data["type"]
        episodes = data["episodes"]
        status = data["status"]
        score = data["score"]
        popularity = data["popularity"]
        year = data["year"] if data["year"] else "N/A"
        genres = ", ".join(genre["name"] for genre in data["genres"])

        # Create an embed message
        embed = discord.Embed(title=title, description=synopsis, color=0xF9D342)
        embed.set_thumbnail(url=image_url)  # Set the image at the top right

        # Add a field for the trailer
        embed.add_field(name="Type", value=anime_type, inline=True)
        embed.add_field(name="Episodes", value=episodes, inline=True)
        embed.add_field(name="Status", value=status, inline=True)
        embed.add_field(name="Score", value=score, inline=True)
        embed.add_field(name="Popularity", value=popularity, inline=True)
        embed.add_field(name="Year", value=year, inline=True)
        embed.add_field(name="Genres", value=genres, inline=False)
        embed.add_field(name="Trailer", value=f"[Watch Here]({trailer_url})", inline=False)
        return embed
    else:
        embed = discord.Embed(title="No results found", description=f"{query} is not")
        return embed
