# Austin Fratesi
# CS1400 - Z01
# Assignment - Unit6 - Task3

from deck import Deck
from time import sleep
from gronkyutil import convertCardToId
from gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(deck.draw()) # Single line

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortByTitle(playerHand) # Single line
        elif choice == 3:
            sortByGang(playerHand) # Single line
        elif choice == 4:
            searchForCard(playerHand) # Single line
        if choice == 5:
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in hand:
        print(i) # Not a single line. The entire function body

# Add other functions you need below

def sortByTitle(hand):
    print("Selection Sort by Title", end="")
    thinking()
    for i in range(len(hand) - 1):
        currMinIndex = i
        for j in range(i + 1, len(hand)):
            if hand[currMinIndex] > hand[j]:
              currMinIndex = j

        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]

def sortByGang(hand):
    print("Bubble Sort by Gang", end="")
    thinking()
    didSwap = True

    while didSwap:
        didSwap = False
        sortCount = 1

        for i in range(len(hand) - sortCount):
            if hand[i].getID() > hand[i + 1].getID():
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True

            sortCount += 1

def searchForCard(hand):
    num = 0
    print("Search for Card")
    for i in TITLE:
        num += 1
        print("\t" * 2 + "(" + str(num) + ") " + str(i))
    title = eval(input("Choose a Title: "))
    title = TITLE[title - 1]

    num1 = 0
    for i in GANG:
        num1 += 1
        print("\t" * 2 + "(" + str(num1) + ") " + str(i))
    gang = eval(input("Choose a Gang: "))
    gang = GANG[gang - 1]

    key = convertCardToId(title, gang)
    binarySearch(hand, key, title + " of " + gang)

def binarySearch(hand, key, card):
    sortByGang(hand)
    print("Binary Search for " + card)
    low = 0
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == hand[mid].getID():
            print("\t" * 2 + "Congrats! You have that card")
            return
        elif key < hand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
    print("\t" * 2 + "Sorry. You do not have that card")

main()

