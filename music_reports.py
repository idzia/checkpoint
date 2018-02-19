import file_handling
import main_program

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by


    :returns: all albums of given genre
    :rtype: list
    """
    genre_on_list = []
    for i in range(len(albums)):
        genre_on_list.append(albums[i][3])

    if genre in genre_on_list:
        albums_by_genre = []    
        for i in range(len(albums)):
            if albums[i][3] == genre:
                albums_by_genre.append(albums[i])
    else:
        raise ValueError("Wrong genre type")
    
    return albums_by_genre

#artist name,album name,release year,genre,length
"""albums = file_handling.import_data(filename='albums_data.txt')
genre = main_program.get_input("Please enter genre: rock")
print(get_albums_by_genre(albums, genre))"""


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    genre_stats = {}
    for i in range(len(albums)):
        if albums[i][3] in genre_stats:
            genre_stats[albums[i][3]] += 1
        else:
            genre_stats[albums[i][3]] = 1
    return genre_stats 

#artist name,album name,release year,genre,length
"""albums = file_handling.import_data(filename='albums_data.txt')
print(get_genre_stats(albums))"""

def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    
    earliest = albums[0][2]
    last_oldest = albums[0]

    for i in range(len(albums)-1):
        if int(earliest) >= int(albums[i+1][2]):
            earliest = albums[i+1][2]
            last_oldest = albums[i+1]
        
            
    return last_oldest   
    

#artist name,album name,release year,genre,length
"""albums = file_handling.import_data(filename='albums_data.txt')
print(get_last_oldest(albums))"""

def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    albums_list_by_genre = get_albums_by_genre(albums, genre)
    last_oldest_of_genre = get_last_oldest(albums_list_by_genre)
    
    return last_oldest_of_genre


"""albums = file_handling.import_data(filename='albums_data.txt')
genre = main_program.get_input("Please enter genre: rock ")
print(get_last_oldest_of_genre(albums, genre))"""

def get_longest_album(albums):
    """
    Get album with biggest value in length field

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
       
    biggest_length = albums[0][4].replace(":", ".")
    longest_album = albums[0]

    for i in range(len(albums)-1):
        if float(biggest_length) < float(albums[i+1][4].replace(":", ".")):
            biggest_length = albums[i+1][4].replace(":", ".")
            longest_album = albums[i+1]
  
    return longest_album


#artist name,album name,release year,genre,length
"""albums = file_handling.import_data(filename='albums_data.txt')
print(get_longest_album(albums))"""


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    minutes = []
    secound = []
    time = []
    for i in range(len(albums)):
        time = albums[i][4].split(":")
        minutes.append(int(time[0]))
        secound.append(int(time[1]))

    albums_length = (sum(minutes)*60 + sum(secound))/60
    
    return round(albums_length, 2)
    
    
    
"""albums = file_handling.import_data(filename='albums_data.txt')
print(get_total_albums_length(albums))"""

