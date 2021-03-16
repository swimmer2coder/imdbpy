class Movie:
    """Class for movies"""
    
    def __init__(self, id, title, year, rating, runtime, genres, plot):
        """Initialize movie info"""
        self._id = id
        self._title = title
        self._year = year
        self._rating = rating
        self._runtime = runtime
        self._genres = genres
        self._plot = plot
        
    @property
    def id(self):
        """Return the id"""
        return self._id
    
    @property
    def title(self):
        """Return the title"""
        return self._title
    
    @property
    def year(self):
        """Return the year"""
        return self._year
    
    @property
    def rating(self):
        """Return the rating"""
        return self._rating
    
    @property
    def genres(self):
        """Return the genre(s)"""
        return self._genres
    
    @property
    def runtime(self):
        """Return the runtime"""
        return self._runtime
    
    @property
    def plot(self):
        """Return the plot"""
        return self._plot
        
    def __repr__(self):
        return id
        
    def __str__(self, id, title, year, genres, rating, runtime, plot):
        """Print formatted movie info"""
        print(f"\nMovie Information for '{self._title}'")
        print(f'Title   : {self._title}')
        print(f'Year    : {self._year}')
        print(f'Genres  : {self._genres}')
        print(f'Rating  : {self._rating}')
        print(f'Runtime : {self._runtime}')
        print(f'Plot    : {self._plot}')

      #  return (f'\nMovie Information for {title}\n', f'Title   : {title}\n', f'Year    : {year}\n', f'Genres  : {genres}\n', f'Rating  : {rating}\n', f'Runtime : {runtime}\n', f'Plot    : {plot}\n')
