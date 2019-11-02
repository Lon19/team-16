from StoryNodeStruct import StoryNode


class Game:
    def __init__(self, startNode, players, id):
        self.currStoryState = startNode
        self.players = players
        self.responseCount = 0
        self.optionAVotes = 0
        self.optionBVotes = 0
        self.id = id
        self.allResponsesTaken = False

    def updateCurrState(self):
        if self.optionAVotes > self.optionBVotes:
            self.currStoryState = self.currStoryState.optionA
        else:
            self.currStoryState = self.currStoryState.optionB
        self.responseCount = 0
        self.optionAVotes = 0
        self.optionBVotes = 0
        for p in self.players:
            p.updateState(self.currStoryState)

    def voteOptionLeft(self):
        if (self.allResponsesTaken):
            self.allResponsesTaken = not self.allResponsesTaken
        self.optionAVotes += 1
        self.responseCount += 1
        if self.responseCount == len(self.players):
            self.updateCurrState()
            self.allResponsesTaken = True

    def voteOptionRight(self):
        if (self.allResponsesTaken):
            self.allResponsesTaken = not self.allResponsesTaken
        self.optionBVotes += 1
        self.responseCount += 1
        if self.responseCount == len(self.players):
            self.updateCurrState()
            self.allResponsesTaken = True

    def addPlayer(self, player):
        self.players.append(player)
