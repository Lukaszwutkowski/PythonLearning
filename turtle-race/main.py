import random
from turtle import Turtle, Screen

is_game_on = True
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "blue", "yellow", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
money = 200


while is_game_on:
    ask_screen = screen.textinput(title="Want to play?", prompt="Type 'y for yes or 'n' for no.")
    if ask_screen == "n":
        is_game_on = False
        print(f"You have ${money}")
    else:
        screen.clear()
        all_turtles.clear()
        money_bet = int(screen.textinput(title="How much do you bet?", prompt="Chose by type value."))
        money -= money - money_bet
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
        for turtle_index in range(0, 6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(colours[turtle_index])
            new_turtle.penup()
            new_turtle.goto(x=-230, y=y_positions[turtle_index])
            all_turtles.append(new_turtle)

        if user_bet:
            is_race_on = True

        while is_race_on:

            for turtle in all_turtles:
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_colour = turtle.pencolor()
                    if winning_colour == user_bet:
                        money += money_bet * 4
                        print(f"You've won! The {winning_colour} turtle is the winner!")
                    else:
                        print(f"You've lost! The {winning_colour} turtle is the winner!")

                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)

screen.exitonclick()