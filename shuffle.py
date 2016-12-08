'''Shuffle
Write a method to shuffle a deck of cards. It must be a perfect shuffle -- in
other words, each of the 52! permutations of the deck must be equally likely. 
Assume that you are given a random number generator which is perfect
'''
from random import random

def shuffle(deck):
    for idx,_ in enumerate(deck):
        swap_idx = int(len(deck)*random())
        tmp = deck[swap_idx]
        deck[swap_idx] = deck[idx]
        deck[idx] = tmp    
    return deck

if __name__ == '__main__':
    deck_order = range(52)
    print(shuffle(deck_order))