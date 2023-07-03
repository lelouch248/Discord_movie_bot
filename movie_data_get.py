import requests
import discord


def get_movie_data(movie_name):
    API_KEY = '9277c4362eea45da57fcca447fa702db'
    url = "https://api.themoviedb.org/3/search/movie"
    query = movie_name
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5Mjc3YzQzNjJlZWE0NWRhNTdmY2NhNDQ3ZmE3MDJkYiIsInN1YiI6IjY0YTE2NjJhMGNiMzM1MDEzOGZkNTMxYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FzLzW06FI6bmAbDgShv5dGSqdshRK8whgG-gI_ZVkKY"
    }

    params = {
        "query": query,
        "include_adult": "true",
        "include_video": "true",
        "sort_by": "popularity.desc"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data["results"]:
        return data["results"][0]  # Assuming the first result is the closest match
    return None


def create_movie_response(movie_data):
    movie_name = movie_data["title"]
    movie_rating = movie_data["vote_average"]
    summary = movie_data["overview"]
    poster_path = movie_data["backdrop_path"]
    release_date = movie_data["release_date"]
    original_title = movie_data["original_title"]
    genre_ids = movie_data["genre_ids"]
    movie_id = movie_data["id"]
    movie_id_data = get_movie_by_id(movie_id)
    tagline = movie_id_data.get("tagline", "")

    # Convert genre IDs to genre names (You may need to map genre IDs to genre names using the TMDb API)
    genre_names = get_genre_names(genre_ids)

    embed = discord.Embed(title=f"Movie Name: {movie_name}",
                          description=f"Rating: {movie_rating}\n\nSummary:\n{summary}", color=0xF9D342)
    embed.set_image(url=f"https://image.tmdb.org/t/p/original{poster_path}")
    embed.add_field(name="Original Title", value=original_title, inline=False)
    embed.add_field(name="Release Date", value=release_date, inline=False)
    embed.add_field(name="Genres", value=", ".join(genre_names), inline=False)
    embed.add_field(name="Tagline", value=tagline, inline=False)

    return embed


def get_movie_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5Mjc3YzQzNjJlZWE0NWRhNTdmY2NhNDQ3ZmE3MDJkYiIsInN1YiI6IjY0YTE2NjJhMGNiMzM1MDEzOGZkNTMxYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FzLzW06FI6bmAbDgShv5dGSqdshRK8whgG-gI_ZVkKY"
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_genre_names(genre_ids):
    # You need to map genre IDs to genre names using the TMDb API or a predefined mapping.
    # Here, we'll just use a simple dictionary as an example.
    genre_mapping = {
        28: "Action",
        12: "Adventure",
        16: "Animation",
        35: "Comedy",
        80: "Crime",
        99: "Documentary",
        18: "Drama",
        10751: "Family",
        14: "Fantasy",
        36: "Histroy",
        27: "Horror",
        10402: "Music",
        9648: "Mystery",
        10749: "Romance",
        878: "Science Fiction",
        10770: "TV Movie",
        53: "Thriller",
        10752: "War",
        37: "Western"

    }

    genre_names = [genre_mapping.get(genre_id, "Unknown") for genre_id in genre_ids]
    return genre_names
