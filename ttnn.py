import ospd
def toupper(s):
    return s.upper()
all_words = map(toupper, ospd.ospd())

def wordtest(word, playerhand):
    hand = {l:playerhand.count(l) for l in playerhand}
    for letter in word:
        if letter in hand:
            hand[letter]-=1
            if hand[letter]<0:
                return False
        else:
            return False
    return True


letter_freq = {
    'A' : 0.08167,
    'B' : 0.01492,
    'C' : 0.02782,
    'D' : 0.04253,
    'E' : 0.12702,
    'F' : 0.02228,
    'G' : 0.02015,
    'H' : 0.06094,
    'I' : 0.06966,
    'J' : 0.00153,
    'K' : 0.00772,
    'L' : 0.04025,
    'M' : 0.02406,
    'N' : 0.06749,
    'O' : 0.07507,
    'P' : 0.01929,
    'Q' : 0.00095,
    'R' : 0.05987,
    'S' : 0.06327,
    'T' : 0.09056,
    'U' : 0.02758,
    'V' : 0.00978,
    'W' : 0.02360,
    'X' : 0.00150,
    'Y' : 0.01974,
    'Z' : 0.00074,
    }

target_size = 100
letter_array = []

for letter in letter_freq:
    freq = max(0.01, letter_freq[letter])
    letter_array += int(freq * target_size) * [letter]


import random

def rand_letter():
    n = len(letter_array)
    return letter_array[random.randint(0, n-1)]


def rand_set():
    s = []
    for _ in 6*[1]:
        s += [rand_letter()]
    return s

print ''

common_letters = rand_set()

print " ".join(common_letters)


import getpass

print ''

numPlayers = 2
pletter = numPlayers * ['']

for i in range(0, numPlayers):
    pletter[i] = getpass.getpass("Player " + str(i+1) + ", enter your seventh letter, IF YOU PLEASE ").upper()[0]

print ''

hands = numPlayers * [[]]
for i in range(0, numPlayers):
    hands[i] = common_letters + [pletter[i]]
    print "Player " + str(i+1) + " letters: " + " ".join(hands[i])

print ''


skillLevel = 3
wordsSoFar = []

def check_word(word, hand):
    if len( word ) > len(hand):
        print 'THIS WORD IS TOO LONG'
        return False

    if len( word ) < skillLevel:
        print 'THIS WORD IS TOO SHORT'
        return False

    if not( word in all_words ):
        print 'KLAXON KLAXON ' + word + ' IS NOT A WORD!'
        return False

    if not wordtest( word, hand ):
        print 'YOU CANNOT MAKE THIS WORD WITH THE LETTERS IN YOUR HAND'
        return False

    if word in wordsSoFar:
        print 'THAT WORD HAS ALREADY BEEN USED'
        return False

    wordsSoFar.append(word)
    return True


playerNumber = 0
while True:

    hand = hands[playerNumber]

    print ' '.join(hand)
    word = raw_input('Player ' + str(playerNumber+1) + ' enter a word, IF YOU PLEASE ').upper()

    if check_word(word, hand):
        print 'POINTS'

    playerNumber = (playerNumber + 1) % numPlayers
    print ''


