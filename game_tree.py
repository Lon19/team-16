import flask
from flask import request, jsonify

class node:
    def __init__(self,event = None, l_button = None, r_button = None, lc = None , rc = None):
        self.event = event
        self.l_button = l_button
        self.r_button = r_button
        self.lc = lc
        self.lc = rc

class game_tree:
    def __init__(self,curr = node(),sentiment = 0, resources = 0):
        self.curr = curr
        self.sentiment = sentiment
        self.resources = resources

    def set_curr(self,event = None, l_button = None, r_button = None, lc = None , rc = None):
        self.curr = node(event,l_button,r_button,lc,rc)

    def decide_next_node(self,action):
        if action == 'l':
            self.curr = self.curr.lc
        else:
            self.curr = self.curr.rc

    def get_card(self):
        return{"Event:":a.event,"Left decision:": a.l_button,"Right decision:":a.r_button}


a = node('where to go?','mars','venus',node('alien','u r dead'))
b = game_tree(a)

b.decide_next_node('l')
print(b.get_card())
'''
b.get_card()
'''

app = flask.Flask(__name__)
app.config["DEBUG"] = True
game = game_tree()

@app.route("/", methods=['PUT'])
def return_action():
    action = str(request.data.get('text', ''))
    next_action = game.decide_next_node(action)
    return jsonify(next_action)

