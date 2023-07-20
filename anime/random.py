import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()


def random_anime():
    url = "https://api.jikan.moe/v4/random/anime"
    response = requests.get(url)
    data = response.json()['data']
    image_url = data['images']['jpg']['large_image_url']
    title = data['title']
    anime_type = data['type']
    episodes = data['episodes']
    status = data['status']
    score = data['score']
    popularity = data['popularity']
    scored_by = data['scored_by']
    # studios = data['studios'][0]['name']
    synopsis = data['synopsis']
    genres = [genre['name'] for genre in data['genres']]
    anime_url = data['url']

    embed = discord.Embed(title=title, url=anime_url, color=0xF9D342)
    embed.set_image(url=image_url)
    embed.add_field(name="Type", value=anime_type, inline=True)
    embed.add_field(name="Episodes", value=episodes, inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Score", value=score, inline=True)
    embed.add_field(name="Popularity", value=popularity, inline=True)
    embed.add_field(name="Scored By", value=scored_by, inline=True)
    # embed.add_field(name="Studios", value=studios, inline=True)
    embed.add_field(name="Synopsis", value=synopsis, inline=False)
    embed.add_field(name="Genres", value=", ".join(genres), inline=False)

    return embed