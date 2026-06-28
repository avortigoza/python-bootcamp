def add(song, playlist):

    new_song = {
        "title": title,
        "singer": singer,
    }

    playlist.append(new_song)

def remove(song, playlist):
    index = int(input("Enter song index: "))
    playlist.pop(index)

def play(playlist):
    """TODO: Print the first song in the playlist (if any) and remove"""
    index = int(input("Enter song index: "))
    print(inventory[index]) and playlist.pop(index)

def show_all(playlist):
    for print_details in playlist:
        print("Song: ")

        for key, value in print_details.items():
            print(f"\t {key}: {value}")

# def save(playlist, filepath):
#     """Challenge: TODO: Save current playlist to filepath"""
#
# def load(filepath):
#     """Challenge: TODO: Load a new playlist from filepath and return it"""

def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
        then do the task requested
    """
    playlist = []
    end = False

    while not end:
        user_choice = input("Select command: ")

        # Ask all inputs in the playlist_app() function to make functions simple
        if user_choice == "add":
            title = input("Enter song name: ")
            singer = input("Enter singer: ")
            add(new_song, playlist)
        if user_choice == "exit":
            end = True

playlist_app()