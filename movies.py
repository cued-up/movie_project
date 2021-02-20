movies = [
    {'title': 'movie 1', 'year': 2001},
    {'title': 'movie 2', 'year': 2002},
    {'title': 'movie 3', 'year': 2006},
    {'title': 'movie 4', 'year': 2004}
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

prompt = 'enter A for adding, D for displaying, F for finding, or Q for quitting: '

def main():
    selection = input(prompt)
    while selection.lower() != 'q':
        if selection.lower() == 'a':
            add_movie()
        elif selection.lower() == 'd':
            display_movie()
        elif selection.lower() == 'f':
            find_movie()
        else:
            print('Invalid input')

        selection = input(prompt)


main()
