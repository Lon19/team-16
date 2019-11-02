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
    # optionA = StoryNode("venus", "you chose venus", endNode, endNode)
    # optionB = StoryNode("mars", "you chose mars", endNode, endNode)
    # root = StoryNode(
    #     "start", "which planet do you want to explore?", optionA, optionB)
    earth = StoryNode("earth",
              "Welcomed as heroes for conquering Mars, we decide to leave further conquest for the future and celebrate our success!",
              endNode,
              endNode)

    no = StoryNode("no",
              "Brexit occurs, changing the course of history. We are dragged back to the year 2100 where we are now at war with the Martians. We join the fight and win, where do we go next?",
              endNode, earth)

    yes = StoryNode("yes",
              "It's a trap! They send us into the nearest wormhole and we go back into the year 2019. Brexit is about to occur. Do we tell the Brits the outcome and prevent Brexit?",
              endNode, no)

    keep = StoryNode("keep","You kept the gold",endNode,endNode)

    offer = StoryNode("offer",
              "The aliens are very happy with your peace offering. They offer to take you to Uranus (a gas giant) on their fastest ship. Do you accept?",
              yes, endNode)

    peace = StoryNode("peace",
              "The aliens demand an offering of peace. They want us to mine 5 tonnes of gold (truly the universal currency). After mining it, a sneaky thought occurs to us: should we keep the gold instead?",
              keep, offer)
    fight = StoryNode('fight','you fought and failed!',endNode,endNode)

    mars = StoryNode("mars",
              "Aliens! The myths about martians were real after all. How should we face the aliens?",
              fight, peace)

    venus = StoryNode("venus",
              "you chose venus",
              endNode,
              endNode)

    root = StoryNode("start",
                     "It is the year 2100. You are an astronaut from the Zetta Corporation. Your mission: make the solar system ours. Be warned, there will be obstacles in your way. Which planet do you want to explore?",
                     mars, venus)

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
