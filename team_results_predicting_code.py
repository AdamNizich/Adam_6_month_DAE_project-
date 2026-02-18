
while True:

    print("Welcome!")

    player_count = int(input("How many players per team? "))

    print("\nTeam 1")

    team1_total = 0

    for i in range(player_count):
        name = input("Enter player name: ")
        overall = int(input("Enter player overall: "))
        team1_total += overall 

    print("\nTeam 2")

    team2_total = 0 

    for i in range(player_count):
        name = input("Enter player name: ")
        overall = int(input("Enter player overall: "))
        team2_total += overall 

    print("\nResults:")
    print("Team 1 total:", team1_total)
    print("Team 2 total:", team2_total)

    if team1_total > team2_total:
        print("Team 1 wins!")
    else:
        print("Team 2 wins!")

    again = input("\nPredict again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you!")
        break
