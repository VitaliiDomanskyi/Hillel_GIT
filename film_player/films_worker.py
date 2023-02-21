import os


class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating, year,
                 budget, box_office, is_profitable, is_oscar_nominated, is_oscar_win, trailer):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.is_profitable = is_profitable
        self.is_oscar_nominated = is_oscar_nominated
        self.is_oscar_win = is_oscar_win
        self.trailer = trailer
        self.storage_address = ''

    def get_info(self):
        info = f"Title: {self.title}\n"
        info += f"Description: {self.description}\n"
        info += f"Director: {self.director}\n"
        info += f"Writer: {self.writer}\n"
        info += f"Cast: {', '.join(self.cast)}\n"
        info += f"Running time: {self.running_time} minutes\n"
        info += f"Country: {self.country}\n"
        info += f"Language: {self.language}\n"
        info += f"IMDb rating: {self.imdb_rating}\n"
        info += f"Year: {self.year}\n"
        info += f"Budget: {self.budget}\n"
        info += f"Box office: {self.box_office}\n"
        info += f"Profitable: {self.is_profitable}\n"
        info += f"Oscar nominated: {self.is_oscar_nominated}\n"
        info += f"Oscar win: {self.is_oscar_win}\n"
        info += f"Trailer: {self.trailer}\n"
        return info

    def upload_file(self):
        filename = self.title.replace(' ', '_') + '.txt'
        first_letter = self.title[0].upper()
        dir_path = os.path.join(os.path.dirname(__file__), 'film_storage', first_letter)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'w') as file:
            file.write('Це текст-заповнювач для ' + self.title)
        self.storage_address = file_path

    def get_film_address(self):
        if self.storage_address:
            return self.storage_address
        else:
            return 'Фільм ще не завантажено'


crazy_stupid_love = Film(
    "Crazy, Stupid, Love.",
    "A middle-aged husband's life changes dramatically when his wife asks him for a divorce. He seeks to rediscover "
    "his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars.",
    "Glenn Ficarra, John Requa",
    "Dan Fogelman",
    ["Steve Carell", "Ryan Gosling", "Julianne Moore"],
    118,
    "United States",
    "English",
    7.4,
    2011,
    "$50 million",
    "$145 million",
    True,
    False,
    False,
    "https://www.imdb.com/video/vi3722091801/")


