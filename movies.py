import logging

logging.basicConfig(filename='activity.log' ,level=logging.INFO)

movies = [
    {'title': 'movie 1', 'year': 2001},
    {'title': 'movie 2', 'year': 2002},
    {'title': 'movie 3', 'year': 2006},
    {'title': 'movie 4', 'year': 2004},
    {'title': 'movie 5', 'year': 2009}
]

def add_movie():
    get_title = input('Enter the title of the movie: ')
    get_year = input('Enter the year: ')

    movies.append(
    {
        'title': get_title,
        'year': get_year
        }
    )
    logging.info(f"User added a movie {get_title.title()} in {get_year}")

def display_movie():
    for movie in movies:
        print(f"Movie Title: {movie['title']}")
        print(f"Movie Year: {movie['year']}")


def find_movie():
    get_title = input('Enter the title of the movie: ')

    for movie in movies:
        if movie['title'] == get_title:
            print(f"Movie Title: {movie['title']}")
            print(f"Movie Year: {movie['year']}")
            logging.info(f"User is searching for {movie['title']} in {movie['year']}")

prompt = 'enter a for adding, d for displaying, f for finding, or q for quitting: '

def main():
    selection = input(prompt)
    logging.info(f'User inputed {selection}')

    while selection.lower() != 'q':

        if selection.lower() == 'a':
            add_movie()
            logging.info('User added a movie')

        elif selection.lower() == 'd':
            display_movie()
            logging.info('User displaying the existing movies')
            
        elif selection.lower() == 'f':
            find_movie()
            logging.info('User is searching for a movie')

        else:
            print('Invalid input')
            logging.info('User inputted an invalid value.')

        selection = input(prompt)
    logging.info('User quitted the app.')


main()
