"""Skapa en datastruktur med en “normal/poker” kortlek med 52 kort, inga jokrar.
Skriv ut kortleken i konsollen, varje kort ska innehålla sin färg, sitt namn och sitt värde (så att det går att räkna med korten),
Blanda kortleken, skriv ut den blandade kortleken i konsollen."""


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

    def __str__(self):
        return str(self.build)


deckOfCards = Deck()
print(deckOfCards)
