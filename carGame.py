while True:
    command = input(">")
    if command.lower() == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command.lower() == "start":
        print("Car started... Ready to go")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "quit":
        print("Game over")
        break
    else:
        print("I don't understand that")
