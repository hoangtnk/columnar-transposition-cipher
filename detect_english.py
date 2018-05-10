# Detect if a certain word is English

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + " \t\n"


def load_dictionary():
    """Load dictionary file."""

    with open("dictionary.txt") as f:
        english_words = {}
        for word in f.read().splitlines():
            english_words[word] = None
    return english_words


ENGLISH_WORDS = load_dictionary()


def get_english_count(msg):
    """Count English words in a message.

    :param msg: the input message
    :type msg: str

    :return: a float represents percentage of English words in the message
    """

    msg = msg.upper()
    msg = remove_non_letters(msg)
    possible_words = msg.split()

    if possible_words == []:
        return 0.0  # no English words in the message

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)


def remove_non_letters(msg):
    """Remove non-letter characters from a message.

    :param msg: the input message
    :type msg: str

    :return: a message containing only letter characters
    """

    letters_only = [symbol for symbol in msg if symbol in LETTERS_AND_SPACE]
    return ''.join(letters_only)


def is_english(msg, word_percentage=20, letter_percentage=85):
    """Determine if a message is English.

    :param msg: the input message
    :type msg: str

    :param word_percentage: the percentage of English words in the message
    :type word_percentage: int

    :param letter_percentage: the percentage of letters in the message
    :type letter_percentage: int

    :return: True if the message is English else False
    """

    words_match = get_english_count(msg) * 100 >= word_percentage
    num_letters = len(remove_non_letters(msg))
    msg_letters_percentage = float(num_letters) / len(msg) * 100
    letters_match = msg_letters_percentage >= letter_percentage
    return words_match and letters_match
