from bs4 import BeautifulSoup as b
import requests as r

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = r.get(URL).text

soup = b(response, "html.parser")

movies = soup.find_all(name="h3", class_="jsx-2692754980")
print(movies)

movie_titles = [movie.getText() for movie in movies]

movies_to_watch = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies_to_watch:
        file.write(f"{movie}\n")




