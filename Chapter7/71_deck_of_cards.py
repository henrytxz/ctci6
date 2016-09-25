# Design
# the
# data
# structures
# for a generic deck of cards.Explain how you would
# subclass
# the
# data
# structures
# to
# implement
# blackjack.
#
# ambiguity?
#
# 54
# cards, 2
# jokers, 4
# suits
# of
# 13,
# from A to
#
# King
#
# objects and their
# relationships:
# game: goal = > till
# everyone
# holds or busts
# player: a
# list
# of
# players in turn
# they
# either
# hit or hold
# hand: the
# cards
# one
# holds
# dealer: deals and goes
# last, is a
# special
# player
# deck: is made
# of
# 52
# cards
# card: a
# suit and a
# value(1
# to
# 13)
# suit: heart, spade, club and diamond
# value: 1
# to
# 13, A
# to
# King
# ace: the
# ace is a
# card
# but
# its
# value
# can
# be
# either
# 1 or 11
#
# total
# value
# of
# a
# deck
# of
# cards is (1 + 2 +.. + 13)*4 = 91 * 4
#
# actions:
# deck
# needs
# a
# shuffle
# operation
# game
# starts, every
# player
# gets
# 2
# cards(
#
#
# def start)
#
#     , dealer
# too,
# with 1 card facing up
# player will have a list of actions to choose from (hold or hit for blackjack, raise, fold, etc.for poker)
# game tracks players who are still in the game ( if one goes bust, remove player from players that are alive)
# hand has a total method, the ace counts as a 10 if total <= 21, else it counts as a 1
# game needs a count method (once everyone is done, has anyone beat the dealer)
#
# blackjack probably doesn't have jokers
#
# deck.shuffle()

# import itertools
import random

class DeckOfCards(object):
    @staticmethod
    def get_deck(jokers=True):
        deck = [value for suit in ['H', 'S', 'C', 'D'] for
                     value in [i + 1 for i in range(13)]]
        if jokers:
            deck.append('small_joker')
            deck.append('big_joker')
        return deck

class Player(object):
    def __init__(self):
        self.hand = []

class CardGame(object):
    def __init__(self, number_players):
        self.cards = self.init_cards()
        random.shuffle(self.cards)
        self.players = []
        for i in range(number_players):
            self.players.append(Player())
        self.active_players = self.players[:]

    def init_cards(self):
        raise NotImplementedError(
            'please provide your implementation for the specific card game')

    def next_card(self):
        return self.cards.pop()

    def deal(self, player):
        player.hand.append(self.next_card())

class BlackJack(CardGame):
    def __init__(self, number_players):
        super(BlackJack, self).__init__(number_players)
        self.dealer = self.players[-1]

    def init_cards(self):
        # assuming the number of players is such that 1 deck suffices
        cards = DeckOfCards.get_deck(jokers=False)
        return cards

    def deal_first_round(self):
        for i in range(2):
            for player in self.players:
                self.deal(player)

    def sum_player_hand(self, player):
        player_hand = [card if card <= 10 else 10 for card in player.hand]
        return sum(player_hand)

    def deal(self, player):
        player.hand.append(self.next_card())
        player_score = self.sum_player_hand(player)
        if player_score > 21:
            print 'player {} went bust with {} points'\
                .format(self.players.index(player), player_score)
            self.active_players.remove(player)

    def play(self):
        self.deal_first_round()
        while self.active_players:
            for player in self.active_players:
                player_move = 'TBD'
                while (player_move != 'y' and player_move != 'n'):
                    player_move = raw_input('player {0}, your hand is {1}, '
                              'do you want another card? y for yes, n for no\n'
                              .format(self.players.index(player), player.hand))
                if player_move == 'y':
                    self.deal(player)
                else:
                    self.active_players.remove(player)
        winner = []
        winning_score = -1
        for player in self.players:
            player_score = self.sum_player_hand(player)
            if player_score <= 21:
                if player_score > winning_score:
                    winner = []
                    winner.append(str(self.players.index(player)))
                    winning_score = player_score
                elif player_score == winning_score:
                    winner.append(str(self.players.index(player)))
        if len(winner) == 0:
            print 'zero winner, something went wrong'
        elif len(winner) == 1:
            print 'winner is {0}, with {1} points'\
            .format(winner[0], winning_score)
        else:
            print 'there is a tie, player {0} tied with score {1}'\
                .format(' and '.join(winner), winning_score)

class Poker(CardGame):
    def init_cards(self):
        # 2 decks
        cards = []
        for i in range(2):
            cards.extend(DeckOfCards(jokers=True))

if __name__ == '__main__':
    game = BlackJack(2)
    # print game.next_card()
    # print game.next_card()
    game.play()

    """ how to only show a player his/her cards?
        perhaps we make this an online game,
        wait for more than 1 player in the game room/at the blackjack table
        1 of them presses, start game
        for each player, have a show_message method
        when waiting for 1 player to react, let other players see "player i's move" on their screen
    """





