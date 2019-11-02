from flask import Flask
from flask import request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
from Game import Game
from StoryNodeStruct import StoryNode
from Player import Player

app = Flask(__name__)
CORS(app)

games = {}


def init_game(game_id):
    endNode = StoryNode("end", "you reached the end", None, None)
    optionA = StoryNode("venus", "you chose venus", endNode, endNode)
    optionB = StoryNode("mars", "you chose mars", endNode, endNode)
    root = StoryNode(
        "start", "which planet do you want to explore?", optionA, optionB)

    players = []
    new_game = Game(root, players, game_id)
    games[new_game.id] = new_game


@app.route("/")
def starting():
    print("hello")
    return "hello"


# @app.route("/<user_id>", methods=["PUT", "GET"])
# def start_game(user_id):
#     init_game()
#     game = games[12345]
#     state = game.currStoryState
#     player = Player(state, user_id)
#     game.addPlayer(player)
#     return jsonify(name=state.name, desc=state.description)


@app.route("/<int:game_id>/<int:user_id>", methods=["PUT", "GET"])
def join_game(game_id, user_id):
    if (not game_id in games):
        init_game(game_id)
    game = games.get(game_id)
    state = game.currStoryState
    game.addPlayer(Player(state, user_id))
    return jsonify(name=state.name, desc=state.description,
                   childA=state.optionA.name, childB=state.optionB.name)


@app.route("/<int:game_id>/left", methods=["GET", "PUT"])
def choose_left(game_id):
    game = games.get(game_id)
    game.voteOptionLeft()
    while(not game.allResponsesTaken):
        pass
    state = game.currStoryState
    if (state == None):
        del games[game_id]
    return jsonify(name=state.name, desc=state.description,
                   childA=state.optionA.name, childB=state.optionB.name)


@app.route("/<int:game_id>/right", methods=["GET", "PUT"])
def choose_right(game_id):
    game = games.get(game_id)
    game.voteOptionRight()
    while(not game.allResponsesTaken):
        pass
    state = game.currStoryState
    if (state == None):
        del games[game_id]
    return jsonify(name=state.name, desc=state.description,
                   childA=state.optionA.name, childB=state.optionB.name)

# add leave game functionaltiies


app.run(port=8080, debug=1)
