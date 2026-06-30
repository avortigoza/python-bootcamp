def add(song, playlist):
    playlist.append(song)

def remove(song, playlist):
    if song in playlist:
        playlist.remove(song)
    else:
        print("Song not in playlist.")

def play(playlist):
    if playlist:
        song = playlist.pop(0)
        print(f"Now playing: {song}.")
    else:
        print("No song in playlist.")

def show_all(playlist):
    for index, song in enumerate(playlist, 1):
        print(f"{index}. {song}")

# def save(playlist, filepath):
#     """Challenge: TODO: Save current playlist to filepath"""


# def load(filepath):
#     """Challenge: TODO: Load a new playlist from filepath and return it"""

def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
        then do the task requested
    """
    playlist = []
    ask = True

    while ask:
        user_choice = input("Select command: ")

        # Ask all inputs in the playlist_app() function to make functions simple
        if user_choice == "add":
            new_song = input("Enter song name: ")
            add(new_song, playlist)
        if user_choice == "remove":
            song = input("Enter song name: ")
            remove(song, playlist)
        if user_choice == "show":
            show_all(playlist)
        if user_choice == "play":
            play(playlist)
        if user_choice == "exit":
            print("Exiting the app...")
            ask = False
        else:
            print("Enter a valid command.")

playlist_app()