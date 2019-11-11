# monster game practice
from random import randint
game_run = True
game_results = []


def create_random(monster_min, monster_max):
    return randint(monster_min, monster_max)


def game_end(winner_name):
    #print(f"{winner_name} has won.")
    print("{} has won".format(winner_name))
    print("---" * 10)


def show_results():
    for x in game_results:
        print(x)
    print("---" * 10)


while game_run:
    counter = 0
    new_round = True
    player_won = False
    monster_won = False

    player = {"name": "Jagroop", "attack": 11, "heal": 16, "health": 100}
    monster = {"name": "PY", "attack_min": 10, "attack_max": 20, "health": 100}
    print("Enter your name")
    player["name"] = input()

    print(player["name"] + "'s health = " + str(player["health"]))
    print(monster["name"] + "'s health = " + str(monster["health"]))

    while new_round:

        counter = counter + 1
        print("---" * 10)
        print("Enter your choice")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit")
        print("4) Show Results")

        player_choice = input()

        if player_choice == "1":
            monster["health"] -= player["attack"]
            player["health"] -= create_random(monster["attack_min"], monster["attack_max"])
            if monster["health"] <= 0:
                player_won = True
            elif player["health"] <= 0:
                monster_won = True
            else:
                print(player["health"])
                print(monster["health"])
        elif player_choice == "2":
            player["health"] += player["heal"]
            player["health"] -= create_random(monster["attack_min"], monster["attack_max"])

            if monster["health"] <= 0:
                player_won = True
            elif player["health"] <= 0:
                monster_won = True
            else:
                print(player["health"])
                print(monster["health"])
        elif player_choice == "3":
            game_run = False
            new_round = False
        elif player_choice == "4":
            show_results()
        else:
            print("Invalid choice")

        if not player_won and not monster_won:
            print(player["name"] + "'s health = " + str(player["health"]))
            print(monster["name"] + "'s health = " + str(monster["health"]))
        elif player_won:
            game_end(player["name"])
            game_state = {"name": player["name"], "health": player["health"], "rounder": counter}
            game_results.append(game_state)
            new_round = False
        elif monster_won:
            game_end(monster["name"])
            game_state = {"name": player["name"], "health": player["health"], "rounder": counter}
            game_results.append(game_state)
            new_round = False