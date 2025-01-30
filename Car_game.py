count = 1
while True:
    taken_input = input(">")
    if taken_input.upper() == "HELP":
        print('''
            start - to start the car
            stop - to stop the car
            quit - to exit the game
            ''')
    elif taken_input.upper() == "START":
        if count == 1:
            print("Car started... Ready to go")
            count += 1
        elif count>1:
            print("Car already started")
    elif taken_input.upper() == "STOP":
        if count == 1:
            print("Car needed to start first")
        elif count == 2:
            print("Car stopped")
            count += 1
        elif count>2:
            print("Car already stopped")
    elif taken_input.upper() == "QUIT":
        print("System ended")
        break
    else:
        print('System do not understand that')
