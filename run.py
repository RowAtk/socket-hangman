import sys
from hangman.server import Server
from hangman.client import Client

def usage():
    """ How to start game (help user to execute code) """
    print("HERE IS HOW YOU USE THIS PROPERLY....\n")
    print("python run.py --[type(server/client)] [name of controller]")
    print("eg. python3.7 run.py --client player1")
    exit(0)

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 3:
        if args[1] == "--client" or args[1] == "-c":
            controller = Client(args[2])
            # controller2 = Server("player")

        elif args[1] == "--server" or args[1] == "-s":
            controller = Server(args[2])
            # controller2 = Server("executioner")
        else:
            usage()
    elif len(args) > 3:
        for i in range(len(args)-3):
            print(f"unknown argument: {args[3]}")
        usage()
    else:
        usage()
    controller.run()
    # controller2.run()

    print("Goodbye")