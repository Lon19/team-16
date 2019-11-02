from StoryNodeStruct import StoryNode


class Game:
    def __init__(self, start_node, players, id):
        self.curr_story_state = start_node
        self.players = players
        self.response_count = 0
        self.option_A_votes = 0
        self.option_B_votes = 0
        self.id = id
        self.all_responses_taken = False

    def updateCurrState(self):
        if self.option_A_votes > self.option_B_votes:
            self.curr_story_state = self.curr_story_state.optionA
        else:
            self.curr_story_state = self.curr_story_state.optionB
        self.response_count = 0
        self.option_A_votes = 0
        self.option_B_votes = 0
        for p in self.players:
            p.updateState(self.curr_story_state)

    def voteOptionLeft(self):
        if (self.all_responses_taken):
            self.all_responses_taken = not self.all_responses_taken
        self.option_A_votes += 1
        self.response_count += 1
        if self.response_count == len(self.players):
            self.updateCurrState()
            self.all_responses_taken = True

    def voteOptionRight(self):
        if (self.all_responses_taken):
            self.all_responses_taken = not self.all_responses_taken
        self.option_B_votes += 1
        self.response_count += 1
        if self.response_count == len(self.players):
            self.updateCurrState()
            self.all_responses_taken = True

    def addPlayer(self, player):
        self.players.append(player)
