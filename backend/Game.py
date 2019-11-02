from StoryNodeStruct import StoryNode

class Game:

    def __init__(self, startNode, players, id):
        self.currStoryState = startNode
        self.players = players
        self.numPlayers = len(players)
        self.responseCount = 0
        self.optionAVotes = 0
        self.optionBVotes = 0
        self.id = id

    def voteOptionA(self):
        self.optionAVotes += 1
        self.responseCount += 1
        if self.responseCount == self.numPlayers:
            updateCurrState()

    def voteOptionB(self):
        self.optionBVotes += 1
        self.responseCount += 1
        if self.responseCount == self.numPlayers:
            updateCurrState()

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
