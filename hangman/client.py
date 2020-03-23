import socket
from hangman.controller import Controller

class Client(Controller):
    """ client for the hangman game """

    def __init__(self, name=''):
        super().__init__(name=name, type="client")
    
    def run(self):
        self.setup()
        self.join_lobby()

        while self.connected:
            # self.connected = False
            pass

    def processMsg(self, msg):
        """ process any messages coming in from server """
        pass
            

    def setup(self):
        """ any code before begining to try and play game (if necessary) """
        # self.connected = False
        pass   

    def join_lobby(self):
        """ join game lobby (connect to game server) """
        try:
            # some code to connect
            self.connected = True
        except Exception:
            print("error connecting to lobby")

    def __repr__(self):
        return super().__repr__()