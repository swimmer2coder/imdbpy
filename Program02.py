# Program02.py
# Maddie Carrigan and Nick Mock

from imdb import IMDb
from movie import Movie
 
ia = IMDb()

keyword = input('Enter a keyword to search:')

movies = ia.search_movie(keyword)

print(f'Search results for {keyword}:')
for i in range(0, 5):
    movie = movies[i]
    print(f"{i + 1}. {movie['title']} ({movie['year']})")

selected = int(input('Enter 1 - 5 to view movie information:'))

id = movies[selected - 1].getID()
movie = ia.get_movie(id)

ia.update(movie, info = ['parents_guide'])


title = movie['title']
year = movie['year']
genres = ', '.join(movie['genres'])
plot = movie['plot'][0]
rating = movie['rating']
runtime = movie['runtime']


# Create movie object
movie_object = Movie(id, title, year, rating, genres, runtime, plot)

#Print movie object
print(movie_object)







### NOTES

# load to movie object instead of just printing to screen 

# ia.update(movie, info = ['parents_guide'])

#program 2 # year = movie['year'] if 'year' in movie else 'NA'

# Create Movie object
#movie_object = Movie(id, title, year, rating, genres, runtime, plot)

# print(f"\nMovie information for '{title}'")

# Print Movie object
#print(movie_object)
