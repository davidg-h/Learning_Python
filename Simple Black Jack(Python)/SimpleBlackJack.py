import random
import os
class Game(object):
    players = []
    card_deck = [i for i in range(2, 11)]
    card_deck.append("J")
    card_deck.append("Q")
    card_deck.append("K")
    card_deck.append("A")

    def hit(self, total):
        index = random.randrange(len(self.card_deck))
        if index < 9:
            total += self.card_deck[index]
        else:
            if self.card_deck[index] == "A":
                if total + 11 <= 21:
                    total += 11
                else:
                    total += 1
            else:
                total += 10
        print("Card: ", self.card_deck[index], "Total: ", total)
        return total

    def comp(self):
        print()
        print("Croupiers turn.")
        compTotal = 0
        while compTotal <= 16:
            compTotal = self.hit(compTotal)
        return compTotal

    def loop(self, hit, player):
        while player.credits > 0 and hit == "y" and player.total < 21:
            player.total = self.hit(player.total)
            if player.total < 21:
                hit = input("Hit? (y/n): ")

    def winCondition(self, compTotal, player):
        if player.total > 21:
            player.credits -= player.stake
            print("You lose")
            print("Player %i credits: " % player.id, player.credits)
        elif compTotal > 21:
            player.credits += player.stake
            print("You win")
            print("Player %i credits: " % player.id, player.credits)
        elif compTotal >= player.total:
            player.credits -= player.stake
            print("You lose")
            print("Player %i credits: " % player.id, player.credits)
        else:
            player.credits += player.stake
            print("You win")
            print("Player %i credits: " % player.id, player.credits)

    def reset(self, inp):
        if inp == "y":
            temp = []
            for player in self.players:
                player.total = 0
                if player.credits != 0:
                    temp.append(player)
                else:
                    print("Player %i has no more chips to play and will be removed!" % player.id)
            self.players = temp
            if self.players.__len__() == 0:
                print("No more Player in the Queue.")
                return False
            return True

    def start(self):
        playerNum = int(input("How many Players would like to play: "))
        for i in range(playerNum):
            self.players.append(Player(i+1))
        print()

        inp = "y"
        while self.reset(inp):
            for play in self.players:
                print()
                print("Player %i credits: " % play.id, play.credits)
                play.stake = int(input("How many chips does Player %i want to bet: " % (play.id)))
                while not(0 < play.stake <= play.credits):
                    print("Wrong input! Try again")
                    play.stake = int(input("How many chips does Player %i want to bet: " % (play.id)))
                for i in range(2):
                    play.total = self.hit(play.total)
                if play.total < 22:
                    hit = input("Hit? (y/n): ")
                    self.loop(hit, play)

            comp = self.comp()
            for player in self.players:
                self.winCondition(comp, player)
            inp = input("Do you want to play again? (y/n): ")
            os.system('cls||clear')

class Player(object):
    def __init__(self, id):
        self.credits = 10
        self.id = id
        self.total = 0

g = Game()
g.start()