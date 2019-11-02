class node:
    def __init__(self,event = None, img = '', l_button = None, r_button = None):
        self.event = event
        self.img = img
        self.l_button = l_button
        self.r_button = r_button
        self.lc = None
        self.lc = None

    def set_lc(self,event = None, img = '',l_button = None, r_button = None):
        self.lc = node(event,img,l_button,r_button)

    def set_rc(self,event = None, img='',l_button = None, r_button = None):
        self.rc = node(event,img,l_button,r_button)


class game_tree(node):
    def __init__(self,curr = node(),sentiment = 0, resources = 0):
        self.curr = curr
        self.sentiment = sentiment
        self.resources = resources

    def set_curr(self,event = None, img='',l_button = None, r_button = None):
        self.curr = node(event,img,l_button,r_button)

    def decide_next_node(self,action):
        if action == 'l':
            self.curr = self.curr.lc
        else:
            self.curr = self.curr.rc

    def get_card(self):
        return {'event': self.curr.event, 'left_decision' : self.curr.l_button,'right_decision' : self.curr.r_button}



