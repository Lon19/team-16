from Game import Game

class Player:

    def __init__(self, state, player_id):
        self.currStoryState = state
        self.player_id = player_id

    def updateState(self, state):
        self.currStoryState = state
