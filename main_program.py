"""
The main program should use functions from music_reports and display modules
"""
import music_reports
import file_handling
import display


def get_input(title):
    question = input(title)
    return question

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """
def handle_menu():
    menu_commands = ["EXIT",
                "Print albums info",
                "Print albums by genre",
                "Print genre stats",
                "Print last oldest",
                "Print last oldest of genre",
                "Print longest album",
                "Print total albums length"
                ]
    display.print_program_menu(menu_commands)

def handle_albums_by_genre(albums):
    genre = get_input("Please enter genre: ")
    albums_data = music_reports.get_albums_by_genre(albums, genre)
    display.print_albums_list(albums_data)

#def handle_genre_stats(albums):



def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    run = True
    while run != False:
        handle_menu()
        albums = file_handling.import_data(filename='albums_data.txt')
        
        try:
            choose = get_input("Please enter from menu: ")
            if choose == "1":
                display.print_albums_list(albums)
            if choose == "2":
                handle_albums_by_genre(albums)
            elif choose == "3":
                handle_genre_stats
            elif choose == "4":
                handle_last_oldest
            elif choose == "5":
                handle_last_oldest_of_genre
            elif choose == "6":
                handle_longest_album
            elif choose == "7":
                handle_total_albums_length
            elif choose == "0":
                run = False
            else:
                raise KeyError("There is no such option.")

        except KeyError as error:
            display.print_error_message(error)
        except ValueError as error:
            display.print_error_message(error)

if __name__ == '__main__':
    
    main()

