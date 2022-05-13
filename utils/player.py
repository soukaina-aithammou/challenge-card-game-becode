import random
from utils.card import Card


class Player:
    def __init__(self, name: str, cards: list, turn_count: int, number_of_cards: int, history: list):
        self.name = name
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def play(self):
        random_card = random.choice(self.cards) #the player choose a card randomly
        self.history.append(random_card) #put the card choosed by the player in history
        for card in self.cards:
            card = str(card)  #the result card is object
            print(f'{self.name} {self.turn_count} played: {card.split()[2]} {card.split()[:2]}')
            print("the history is ", self.history)
            return card


class Deck:
    def __init__(self, cards: list):
        self.cards = cards

    def fill_deck(self):#create a methode that fill a deck with 52 cards
        color = ["black", "red"]
        icon = ['♥', '♦', '♣', '♠']
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for c in color:
            for i in icon:
                for v in value:
                    if i in ['♥', '♦'] and c == 'red':  # here the two symbols are red
                        card = Card(c, i, v)
                        self.cards.append(card)
                    elif i in ['♣', '♠'] and c == 'black':  # here the two symbols are black
                        card = Card(c, i, v)
                        self.cards.append(card)
        return self.cards


    def shuffle(self) -> list:   #create a methode that shuffle the list of  cards
        random.shuffle(self.fill_deck())
        return self.cards        #return the list of cards shuffeld

    def distribute(self, players: list) -> list:
        shuffel_cards = self.shuffle()  #put the shufeld cards in a variable
        number_of_players = len(players) #get the number of players from the list
        distriputed_cards = list()
        #distribute the cards evenly
        chunk_size = len(shuffel_cards) // number_of_players
        if number_of_players % 2 == 0:
            for i in range(0, len(shuffel_cards), chunk_size):
                distriputed_cards.append(shuffel_cards[i:i + chunk_size])
        else:
            print("please enter an even numper of players")
        return distriputed_cards  # return list of list

s=Deck([])
print(s.fill_deck())