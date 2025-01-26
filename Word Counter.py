print ("""--------------------
    WORD COUNTER
--------------------""")

def count_words(word):
    character_count = word.replace(" ", "")
    character_count = len(character_count)
    word_count = len(word.split())
    return  word_count, character_count


while True:
    user_sentence = input("\nEnter a sentence: ")
    word, alphabet = count_words(user_sentence)
    print(f"Your sentence has {word} words and {alphabet} characters.\n")

    again = input("Do you want to try again? (y/n): ")
    if again.lower() != 'y':
        break
