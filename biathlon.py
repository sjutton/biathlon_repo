from random import randint

def printScore(targets):
    print(1,2,3,4,5)
    print(' '.join(targets))

def gameLoop(targets):
    skill = randint(1,4)
    energy = randint(1,4)
    bullets = 1
    points = 0
    
    while bullets < 6:
        recievedShot = int(input(f"Shoot number {bullets} at: "))
        recievedShot -= 1      #Turns input into correlating index.
        print("----------")
        
        if targets[recievedShot] == "O":
            print("Hit on closed target (0 points)")
        else:
            if randint(0,(skill+energy)) > 1:
                print("Hit on open target (1 point)")
                points += 1
                targets[recievedShot] = "O"
            else:
                print("Miss (0 points)") 
        print("----------")
        printScore(targets)
        bullets += 1
    return points
    
    
def main():
    print("--------------------")
    print("      Biathlon\n\n a hit or miss game")
    print("--------------------")
    print("You've got five shots.")
    targets = ["*","*","*","*","*"]
    print("----------")
    printScore(targets)
    points = gameLoop(targets)
    print("Final Score: ", points, "/ 5")


main()