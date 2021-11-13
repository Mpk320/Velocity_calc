# Calculates velocity of an object

# where calculation takes place
def data():
    position = input("Input Change in position(m): ")
    time = input("input Time(s): ")
    result = float(position) / float(time)
    print("Velocity(m/s) = " + str(result))


# to reset calc
def retry():
    redo = input("Enter y to continue or n to quit: ")
    if redo == "y":
        return beginning()
    elif redo == "n":
        print("Have a nice day!")
    else:
        wrong_data()


# loops retry function if y/n are not received
def wrong_data():
    retry()


# runs data and retry functions
def beginning():
    data()
    retry()


beginning()
