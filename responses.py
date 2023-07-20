import random
import movie_data_get
from components import help
from anime import random
from anime import anime_search
from ml import animal


def get_response(message: str) -> str:
    p_message = message.lower()
    if p_message == '!!roll':
        return str(random.randint(1, 6))

    if p_message.startswith("!!movie"):
        movie_name = p_message.split("!!movie")[1].strip()
        movie_data = movie_data_get.get_movie_data(movie_name)
        if movie_data:
            response = movie_data_get.create_movie_response(movie_data)
        return response

    if p_message == '!!help':
        return help.get_help_data()

    if p_message == "!!random anime":
        return random.random_anime()

    if p_message.startswith("!!anime"):
        anime_name = p_message.split("!!anime")[1].strip()
        return anime_search.get_anime_data(anime_name)

    if p_message.startswith("!!idanimal"):
        image_url = p_message.split("!!idanimal")[1].strip()
        return animal.catanddog(message, image_url)
