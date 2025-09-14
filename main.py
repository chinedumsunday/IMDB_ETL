from etl import extract

movies = extract.extract("./data/raw_data/netflix_titles.csv", "movies")

print(extract.explore(movies))


