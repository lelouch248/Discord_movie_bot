import random
import movie_data_get


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '':
        return

    if p_message == '!!hello':
        return 'hey there'

    if message == '!!roll':
        return str(random.randint(1, 6))

    if p_message == '!!help':
        return '`This is the help section that you can modify`'

    if p_message.startswith("!!movie"):
        movie_name = p_message.split("!!movie")[1].strip()
        movie_data = movie_data_get.get_movie_data(movie_name)
        if movie_data:
            response = movie_data_get.create_movie_response(movie_data)
        return response

