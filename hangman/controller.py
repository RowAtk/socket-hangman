import socket

class Controller():
    """ Class representing the controller of this instance of the program.
    In other words, the controller is the driver of the program or the mode it is in.
    There are two controllers: The Server or the Client. 
    """

    idcount = 0
    port = 9090

    def __init__(self, name="", type="normal"):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.idnum = Controller.idcount
            Controller.idcount += 1
            print(f"<{type} socket>{self.idnum}: \'{name}\' created")
            
            print(self.idnum)
        except socket.error as e:
            print(f"failed to create socket \'{name}\' with error {e}")

    def get_free_port(self):
        p = Controller.port
        Controller.port += 1
        return p
    
    def run(self):
        raise NotImplementedError

    def setup(self):
        """ any code to run before controller begin to communicate. 
        For eg. configuration of ports and IP addresses """
        raise NotImplementedError

    def __repr__(self):
        return super().__repr__()