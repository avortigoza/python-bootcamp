def get_longest_word(text):
    words = text.split

    longest_word = ""

    for word in words():
        if len(longest_word) < len(word):
            longest_word = word

    return longest_word


# "The quick brown fox jumps" -> "quick"
print(get_longest_word("The quick brown fox jumps"))

# "I love programming in Python!" -> "programming"
print(get_longest_word("I love programming in Python!"))

# "" -> ""
print(get_longest_word(""))
