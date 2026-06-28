# TODO: Ask the user for a word
# TODO: If the word is in banned_words, say "Banned"

banned_words = ("moist", "break", "raise")
banned_input = input("Enter a word: ")
if banned_input in banned_words:
    print("Banned.")
else:
    print("Accepted.")


