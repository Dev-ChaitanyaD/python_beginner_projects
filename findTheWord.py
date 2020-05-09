'''
Hey there, feel free to implement your logic and also let me know how do you like it...
Also follow mi on Twitter:- @DevDCtech
'''

# Here are the libraries we import
import random
import time

# Here are the lists of various letter's words
listOfFive = ['abyss', 'affix', 'askew', 'axiom', 'azure', 'banjo', 'bayou', 'blitz', 'buxom', 'crypt', 'cycle', 'equip', 'fjord', 'flyby', 'funny', 'gabby', 'gizmo', 'glyph', 'haiku', 'ivory', 'jazzy', 'jelly', 'juicy', 'jumbo', 'kayak', 'kazoo', 'khaki', 'kiosk', 'klutz', 'lucky', 'lymph', 'nymph', 'ovary', 'pixel', 'polka', 'pshaw', 'puppy', 'queue', 'quips', 'staff', 'topaz', 'unzip', 'vixen', 'vodka', 'waltz', 'wimpy', 'woozy', 'yoked', 'yummy', 'zilch']
listOfSix = ['absurd', 'avenue', 'bikini', 'boggle', 'boxcar', 'boxful', 'caliph', 'cobweb', 'duplex', 'exodus', 'faking', 'galaxy', 'gazebo', 'giaour', 'gossip', 'hyphen', 'icebox', 'injury', 'jigsaw', 'jockey', 'joking', 'joyful', 'kitsch', 'larynx', 'luxury', 'matrix', 'oxygen', 'pajama', 'psyche', 'quartz', 'quorum', 'rhythm', 'snazzy', 'sphinx', 'spritz', 'squawk', 'subway', 'swivel', 'uptown', 'voodoo', 'vortex', 'wheezy', 'wizard', 'yippee', 'zigzag', 'zipper', 'zodiac', 'zombie']
listOfSeven = ['awkward', 'buffalo', 'buffoon', 'buzzard', 'buzzing', 'croquet', 'curacao', 'dwarves', 'fixable', 'fuchsia', 'jackpot', 'jaywalk', 'jogging', 'jukebox', 'keyhole', 'lengths', 'marquis', 'mystify', 'naphtha', 'oxidize', 'quizzes', 'rhubarb', 'scratch', 'stretch', 'stymied', 'unknown', 'walkway', 'whiskey']
listOfEight = ['abruptly', 'bagpipes', 'blizzard', 'bookworm', 'buckaroo', 'daiquiri', 'dizzying', 'embezzle', 'fishhook', 'flapjack', 'flopping', 'foxglove', 'frazzled', 'frizzled', 'glowworm', 'gigabyte', 'jaundice', 'jazziest', 'jiujitsu', 'kilobyte', 'knapsack', 'nowadays', 'peekaboo', 'puzzling', 'quixotic', 'rickshaw', 'schnapps', 'strength', 'syndrome', 'unworthy', 'vaporize', 'whizzing', 'whomever', 'youthful']
listOfNine = ['bandwagon', 'beekeeper', 'buzzwords', 'cockiness', 'espionage', 'galvanize', 'gigahertz', 'haphazard', 'kilohertz', 'kiwifruit', 'megahertz', 'microwave', 'nightclub', 'numbskull', 'pneumonia', 'voyeurism', 'xylophone', 'yachtsman', 'youthful']
listOfTen = ['fluffiness', 'grogginess', 'iatrogenic', 'jawbreaker', 'razzmatazz', 'stronghold', 'thriftless', 'thumbscrew', 'transcript', 'transgress', 'transplant', 'triphthong', 'wellspring', 'witchcraft', 'wristwatch', 'zigzagging']

# User will enter his name
name = input('Enter your name: ')

print('Welcome, ', name)

# This input is to enter how many letter's user wanted
letterIP = int(input('How many letters you want in word\n(Please enter range from 5 to 10): '))

def wordFinder(letterIP):
    global wordToFind
    
    # If user entered input unsatisfied with condition then it will prompt again
    # Random word will be choosen from list of no. of letters inputed by user
    while letterIP < 5 or letterIP > 10:
        letterIP = int(input('(Please enter range from 5 to 10): '))
    else:
        print('Ok! Searching...')
        time.sleep(2)
        print('Here is your word')

        if letterIP == 5:
            wordToFind = random.choice(listOfFive)
        elif letterIP == 6:
            wordToFind = random.choice(listOfSix)
        elif letterIP == 7:
            wordToFind = random.choice(listOfSeven)
        elif letterIP == 8:
            wordToFind = random.choice(listOfEight)
        elif letterIP == 9:
            wordToFind = random.choice(listOfNine)
        else:
            wordToFind = random.choice(listOfTen)
    
wordFinder(letterIP)

time.sleep(1)
turns = letterIP + 5
print('Your Turns: ', turns)
guess = ''

while turns > 0:
    
    lost = 0

    # It takes one character from word and checks whether it is in the guess
    for letter in wordToFind:
        if letter in guess:
            print(letter, end=' ')
        else:
            print('#', end=' ')
            lost =+ 1

    # If lost == 0 then user will win and correct word is printed
    if lost == 0:
        print('\nYou win')
        print('Word is', wordToFind)
        break

    # Wrong input will again prompt user to enter character again
    collector = input('\nGuess the character: ')[0]

    # Each input character is stored in guess
    guess += collector

    # This will check input character with word
    # If the character is wrong the it will print 'Wrong'
    # Also it will generate no. of turns left
    # And if the turns == 0 then it will print 'You loose'
    # And the word will be printed
    if collector not in wordToFind:
        turns -= 1
        print('Wrong')
        print('You have ', + turns, 'turns left')
        if turns == 0:
            print('You Loose')
            print('The word is: ', wordToFind)
