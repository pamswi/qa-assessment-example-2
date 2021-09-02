    # <QUESTION 1>

    # Given a word and a string of characters, return the word with all of the given characters
    # replaced with underscores

    # This should be case sensitive

    # <EXAMPLES>

    # one("hello world", "aeiou") → "h_ll_ w_rld"
    # one("didgeridoo", "do") → "_i_geri___"
    # one("punctation, or something?", " ,?") → "punctuation__or_something_"

def one(word, chars):
    pass

    # <QUESTION 2>

    # Given an integer - representing total seconds - return a tuple of integers (of length 4) representing 
    # days, hours, minutes, and seconds

    # <EXAMPLES>

    # two(270) → (0, 0, 4, 30)
    # two(3600) → (0, 1, 0, 0)
    # two(86400) → (1, 0, 0, 0)

    # <HINT>

    # There are 86,400 seconds in a day, and 3600 seconds in an hour

def two(total_seconds):
    pass

    # <QUESTION 3>

    # Given a dictionary mapping keys to values, return a new dictionary mapping the values
    # to their corresponding keys

    # <EXAMPLES>

    # three({'hello':'hola', 'thank you':'gracias'}) → {'hola':'hello', 'gracias':'thank you'}
    # three({101:'Optimisation', 102:'Partial ODEs'}) → {'Optimisation':101, 'Partial ODEs':102}

    # <HINT>

    # Dictionaries have methods that can be used to get their keys, values, or items

def three(dictionary):
    pass

    # <QUESTION 4>

    # Given an integer, return the largest of the numbers this integer is divisible by
    # excluding itself

    # This should also work for negative numbers

    # <EXAMPLES>

    # four(10) → 5
    # four(24) → 12
    # four(7) → 1
    # four(-10) → 5

def four(number):
    pass

    # <QUESTION 5>

    # Given a string of characters, return the character with the lowest ASCII value

    # <EXAMPLES>

    # five('abcdef') → 'a'
    # four('LoremIpsum') → 'I'
    # four('hello world!') → ' '

def five(chars):
    pass

    # <QUESTION 6>

    # Given a paragraph of text and an integer, break the paragraph into "pages" (a list of strings), where the
    # length of each page is less than the given integer

    # Don't break words up across pages!

    # <EXAMPLES>

    # six('hello world, how are you?', 12) → ['hello world,', 'how are you?']
    # six('hello world, how are you?', 6) → ['hello', 'world,', 'how', 'are', 'you?']
    # six('hello world, how are you?', 20) → ['hello world, how are', 'you?']
    
def six(paragraph, limit):
    pass
