from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
from Game import Game
from StoryNodeStruct import StoryNode
from Player import Player

app = Flask(__name__)
CORS(app)

games = {}

@app.route("/")
def start_game():
    endNode = StoryNode("end", "you reached the end", None, None)
    optionA = StoryNode("venus", "you chose venus", endNode, endNode)
    optionB = StoryNode("mars", "you chose mars", endNode, endNode)
    root = StoryNode("start", "which planet do you want to explore?", optionA, optionB)

    players = []
    playerA = Player(root)
    players.append(playerA)
    new_game = Game(root, players, 12345)
    games.add(new_game.id, new_game)

@app.route("/join_game", methods=["GET"])
def join_game():
    player_id = request.args.get('player_id')
    game_id = request.args.get('game_id')
    games.get(game_id).add_player(player_id)

@app.route("/choose_left")
def choose_left():
    
