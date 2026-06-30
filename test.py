def add(song, playlist):
    playlist.append(song)
"""Add song to playlist"""
def remove(song, playlist):
    if song in playlist:
        playlist.remove(song)
    else:
        print("Song does not exist.")
"""Remove song from playlist (if there)"""
def play(playlist):
    if playlist:
        song = playlist.pop(0)
        print(f"Now playing: {song}.")
    else:
        print("There is no existing song.")
"""Print the first song in the playlist and remove"""
def show_all(playlist):
    for index, song in enumerate(playlist, 1):
        print(f"{index}. {song}")

"""Print all contents in the playlist"""

def playlist_app():
    playlist = []
    ask = True
    while ask:
        user_choice = input("Enter a command: ")
        if user_choice == "add":
            new_song = input("Enter song title: ")
            add(new_song, playlist)
        if user_choice == "remove":
            song = input("Enter song title: ")
            remove(song, playlist)
        if user_choice == "play":
            play(playlist)
        if user_choice == "show":
            show_all(playlist)
        if user_choice == "exit":
            print("Exiting the app...")
            ask = False
        else:
            print("Enter a valid command.")

"""While loop that keeps asking for command"""
playlist_app()