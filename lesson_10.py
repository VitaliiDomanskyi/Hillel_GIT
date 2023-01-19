"""Task 4"""

search_1 = lambda x: [film['title'] for film in x if float(film['rating']) > 8.5]
titles = search_1(imdb_rank)
sorted(titles)

"""Task 5"""


def get_trailer(title):
  for film in imdb_rank:
    if film['title'] == title:
      return film['trailer']


get_trailer("North by Northwest")

"""Task 6"""


def film_author(author):
    result = {'author': author, 'quantity': 0, 'films': []}
    for film in imdb_rank:
        if author in film.get('director') or [i for i in film.get('writers') if author in i]:
        result['quantity'] += 1
        movie_info = {'title': film.get('title'),
                    'rating': film.get('rating')}
        result['films'].append(movie_info)
    return result


film_author("Francis Ford Coppola")