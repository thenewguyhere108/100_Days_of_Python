import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

website_content = requests.get(URL)
soup = BeautifulSoup(website_content.content, "html.parser")

# Use the h3 element to filter out all the movie title elements
movie_list = soup.find_all(name="h3", class_="title")

# Use a for loop to isolate and append the titles to a list
movies = [movie.getText() for movie in movie_list]

# Use a for loop to create and write the data into a text file
with open("movie_list.txt", mode="w") as file:
    for i in range(99, -1, -1):
        file.writelines(movies[i]+"\n")
