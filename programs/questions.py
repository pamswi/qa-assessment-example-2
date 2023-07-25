# <QUESTION 1>

def one(word, chars):
 

    # Given a word and a string of characters, return the word with all of the given characters
    # replaced with underscores

    # This should be case sensitive
    for char in chars:
        word = word.replace(char, "_")
    return word

# <QUESTION 2>

    # Given an integer - representing total seconds - return a tuple of integers (of length 4) representing 
    # days, hours, minutes, and seconds


    # <HINT>

    # There are 86,400 seconds in a day, and 3600 seconds in an hour

def two(total_seconds):
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400

    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return days, hours, minutes, seconds


# <QUESTION 3>

    # Given a dictionary mapping keys to values, return a new dictionary mapping the values
    # to their corresponding keys

    # <HINT>

    # Dictionaries have methods that can be used to get their keys, values, or items

def three(dictionary):
    
    new_dict = {}

    # iterate through the key value pairs
    for key, value in dictionary.items():
        # swap the key and value and store in new_dict
        new_dict[value] = key
    return new_dict



# <QUESTION 4>

    # Given an integer, return the largest of the numbers this integer is divisible by
    # excluding itself

    # This should also work for negative numbers


def four(number):
    largest_divisor = 0
    
    if number > 0:
        for i in range(2, number):
            if number % i == 0:
                largest_divisor = i
    elif number < 0:
         for i in range(2, (abs(number))):
            if number % i == 0:
                largest_divisor = i
                

    if largest_divisor == 0:
        return 1 if number != 1 else 0
    else:
        return largest_divisor



# <QUESTION 5>

    # Given a string of characters, return the character with the lowest ASCII value

def five(chars):

    new_dict = {}

    for char in chars:
       new_dict[char] = ord(char)

    value = min(new_dict)
    return min(new_dict)


# <QUESTION 6>

    # Given a paragraph of text and an integer, break the paragraph into "pages" (a list of strings), where the
    # length of each page is less than the given integer

    # Don't break words up across pages!
import textwrap

def six(paragraph, limit):
    
    paragraph_wrap = textwrap.wrap(paragraph, limit)
    return paragraph_wrap



# question 1 tests
# print(one("hello world", "aeiou"))
# print(one("didgeridoo", "do")) # "_i_geri___"
# print(one("punctation, or something?", " ,?")) #  "punctuation__or_something_"

# # question 2 tests
# print(two(270)) #(0, 0, 4, 30))
# print(two(3600)) # → (0, 1, 0, 0)
# print(two(86400)) # → (1, 0, 0, 0)

# # question 3 tests
# print(three({'hello':'hola', 'thank you':'gracias'})) # → {'hola':'hello', 'gracias':'thank you'}
# print(three({101:'Optimisation', 102:'Partial ODEs'})) # → {'Optimisation':101, 'Partial ODEs':102}

# # question 4 tests
# print(four(10)) # → 5
# print(four(24)) # → 12
# print(four(7)) # → 1
# print(four(-10)) # → 5

# question 5 tests
# print(five('abcdef')) # → 'a'
# print(five('LoremIpsum')) # → 'I'
# print(five('hello world!')) # → ' '

# question 6 tests
# print(six('hello world, how are you?', 12)) # → ['hello world,', 'how are you?']
# print(six('hello world, how are you?', 6)) # → ['hello', 'world,', 'how', 'are', 'you?']
# print(six('hello world, how are you?', 20)) # → ['hello world, how are', 'you?']