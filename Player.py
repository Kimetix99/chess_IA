#!/usr/bin/pypy
class Player:

    def __init__ (self, PlayerID, side):
        self.PlayerID=PlayerID
        self.side=side

    def equals(self, player):
        return self.PlayerID == player.PlayerID