import random


class Card:
    """Klass för att hantera ett kort"""

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val


class Deck:
    """Klass för att hantera kortlek"""

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Heart", "Diamond", "Spades", "Club"]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def shuffle(self):
        return random.shuffle(self.cards)

    def drawCard(self):
        card = self.cards[-1]
        self.cards.pop()
        return card

    def show(self):
        for card in self.cards:
            print(f"{card.suit}  {card.value}")

    def add(self, card_to_add):
        return self.cards.extend(card_to_add)

    def length(self):
        return len(self.cards)


class Player:
    """Klass som hanterar en spelare med en hand på fem kort"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def show(self):
        return self.name

    def draw(self, deck, no):
        for i in range(no):
            self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for h in self.hand:
            print(f"{h.suit}  {h.value}")

    def score(self):
        sum = 0
        for h in self.hand:
            sum += h.value
        return sum

    def clear(self, deck):
        deck.add(self.hand)
        self.hand.clear()

    def length(self):
        print(len(self.hand))


class Dealer:
    """Klass som hanterar kortleken"""

    def __init__(self):
        self.currentDeck = Deck()

    def shuffle(self):
        self.currentDeck.shuffle()

    def dealCards(self, player, no):
        for i in range(no):
            player.hand.append(self.currentDeck.drawCard())

    def no_cards(self):
        return self.currentDeck.length()


class AnalyzeHands():

    def score(players):
        scores = []
        for player in players:
            scores.append(player.score())
        return scores


class Game():
    """Klass som hanterar spelet"""

    def __init__(self):
        self.players = []
        self.currentDeck = Deck()

    def start_game():
        pass

    def add_players():
        pass


deckOfCards = Deck()
deckOfCards.shuffle()
player1 = Player("Slim")
player2 = Player("Luke")
player1.draw(deckOfCards, 5)
player2.draw(deckOfCards, 5)
print("---------------------------")
print(f"Player 1: {player1.show()}")
player1.showHand()
print(f"Current score in hand: {player1.score()}")
print("---------------------------")
print("---------------------------")
print(f"Player 2: {player1.show()}")
player2.showHand()
print(f"Current score in hand: {player2.score()}")
print("---------------------------")
print(f"Remaining cards in deck {deckOfCards.length()}")
print("Move both players card to deck")
player1.clear(deckOfCards)
player2.clear(deckOfCards)
print(deckOfCards.length())
print(player1.showHand())
print(player2.showHand())
print("---------------------------")
print("Shuffle deck")
deckOfCards.shuffle()
deckOfCards.show()
print("---------------------------")
print("Dealern blandar kortleken och delar ut var sin hand till båda spelarna")
dealer = Dealer()
dealer.shuffle()
print("----player 1-----")
print(player1.show())
dealer.dealCards(player1, 5)
print(player1.showHand())
print("----player 2-----")
print(player2.show())
dealer.dealCards(player2, 5)
print(player2.showHand())
print("Remaining cards...")
print(dealer.no_cards())
scores = AnalyzeHands.score([player1, player2])
print(f"{player1.show()}: {scores[0]}")
print(f"{player2.show()}: {scores[1]}")
print("---------------------------")
