#
#   Python: 3.12
#   Author: Jennie Smith
#

def start(home=0, adventure=0, name=""):
    # get user's name
    name = describe_game(name)
    explore(home, adventure, name)


def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If ti is not a new game, thank the player for playing again and continue with the game.
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be approached \nby several different people. \nYou can choose to go off adventuring, or stay at home")
                    print("At the end of the game your story \nwill be told over generations.")
                    stop = False
    return name


def explore(home, adventure, name):
    stop = True
    while stop:
        show_score(home, adventure, name)
        pick = input("\nA stranger approaches you to invite \nyou on a quest. Will you go with them on an adventure\nor stay home and cozy? (A/H) \n>>>: ").lower()
        if pick == "a":
            print("\nThe stranger and you take off on your mission...")
            adventure += 1
            stop = False
        if pick == "h":
            print("\nThe stranger looks disappointed \nand heads off on their own, leaving you in your doorway...")
            home += 1
            stop = False
    score(home, adventure, name)  # pass the three variables to the score()
    return None


def show_score(home, adventure, name):
    print("\n{}, your current total: \n({}, Staying Home) and ({}, Adventuring)".format(name, home, adventure))


def score(home, adventure, name):
    # score function is being passed the values stored within the 3 variables
    if home > 2:  # if condition is valid, call win function passing in the variables so it can use them
        cozy(name)
    if adventure > 2:  # if condition is valid, call lose function passing in the variables so it can use them
        traveled(name)
    else:  # else, call nice_mean function passing in the variables as it can use them
        explore(home, adventure, name)


def cozy(name):
    # substitute the {} wildcards with our variable values
    print("\nNice job {}, you successfully avoided messy adventures! \nYou spend your happy evenings \nat home and cozy by your fireplace!".format(name))
    # call again function and pass in our variables
    again(name)


def traveled(name):
    # substitute the {} wildcards with our variable values
    print("\nNice job {}, you went on so many adventures! \nYou made many friends and had many\namazing experiences!".format(name))
    # call again function and pass in our variables
    again(name)


def again(name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")


def reset(name):
    home = 0
    adventure = 0
    # don't reset the variable name since the same user is playing again
    start(home, adventure, name)


if __name__ == "__main__":
    start()
