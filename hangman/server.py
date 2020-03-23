from time import sleep
from hangman.controller import Controller

class Server(Controller):
    """ Server for the socket game """
    MAX_CONNECTIONS = 0 # maximum numbe rof connections server should receive

    def __init__(self, name="", port=None):
        super().__init__(name=name, type="server")
        self.name = name
        self.port = port if port and type(port) == int else self.get_free_port()
        self.alive = True # determines if server should keep running
        self.connections = [] # stores list of connections

    def run(self):
        self.setup()
        self.client_lobby()
        self.status()
        print(self.connections)
        while self.alive:
            # self.alive = False
            pass
    
        self.close_connections()

    def processMsg(self, msg):
        """ process message coming from client """
        pass       

    def status(self):
        if self.alive:
            print(f"<server>{self.name} running...")
        else:
            print(f"<server>{self.name} inactive...")

    def setup(self):
        """ code to run before the actual game can begin """
        self.sock.bind(('', self.port)) # listen for all incomming connections on network
        self.sock.listen(Server.MAX_CONNECTIONS)

    def client_lobby(self):
        """ wait for full lobby to start game (accept max number of client sockets) """
        for i in range(Server.MAX_CONNECTIONS):
            # client = 
            # print(f"client connected from {client[1]}")
            # self.connections.append(client)
            pass

    def close_connections(self):
        """ close client sockets """
        for connection in self.connections:
            connection.close()

    def __repr__(self):
        return super().__repr__()