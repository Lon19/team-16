from Game import Game
from StoryNodeStruct import StoryNode
from Player import Player

endNode = StoryNode("end", "you reached the end", None, None)
optionA = StoryNode("venus", "you chose venus", endNode, endNode)
optionB = StoryNode("mars", "you chose mars", endNode, endNode)
root = StoryNode("start", "which planet do you want to explore?", optionA, optionB)

players = []
playerA = Player(root)
playerB = Player(root)
playerC = Player(root)
players.append(playerA)
players.append(playerB)
players.append(playerC)

Game(root, players)
