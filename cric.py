import random

print('')
print("How many overs would you like to play?\n")
overs = int(input(" "))
print("The game is set for", overs, "overs", '\n')
print('Computer won the toss and chose to bowl first', '\n')
print("You're batting first", '\n')

user_balls = 0
user_total = 0

while user_balls < overs * 6:

    try:

        comp = random.randint(1, 6)
        user = int(input("Enter number\n"))

        if user > 6:
            print("Error: Enter a number between 1 to 6")
        else:
            user_balls += 1
            balls_left = (overs * 6) - user_balls

            if comp == user:
                print("OOPS! You're Out.", "\n")
                print(f"Your total score is {user_total}", '\n')
                break

            else:
                print(f"You've {balls_left} balls left")
                user_total = user_total + user
                print("Your Score is ", user_total)

    except ValueError:
        print("Error: Enter a value between 1 to 6")

print('................................')
print("It's time for computer's batting")
print('................................', '\n')

print("Computer's target is", user_total + 1, '\n')
comp_balls = 0
comp_total = 0

while comp_balls < overs * 6:

    try:

        if comp_total > user_total:
            break

        comp_run = random.randint(1, 6)
        user = int(input("Enter number\n"))

        if user > 6:
            print("Error: Enter a number between 1 to 6")
        else:
            comp_balls += 1
            balls_left = (overs * 6) - comp_balls

            if comp_run == user:
                print("Hurray! That's Out.", "\n")
                print(f"Computer's total score is {comp_total}", '\n')
                break

            else:
                print(f"Computer have {balls_left} balls left")
                comp_total = comp_total + comp_run
                print("Computer's score is ", comp_total, '\n')

    except ValueError:
        print('Error: Enter a number between 1 to 6')

if user_total == comp_total:
    print("The match is tied")
elif user_total > comp_total:
    print("Congrats! You won the match by", user_total - comp_total, "runs")
elif user_total < comp_total:
    print('Computer wins. You lost the match', '\n')
    print('Better luck next time!')

print('...........................')
print("Hit run to restart the game")
print('...........................')
