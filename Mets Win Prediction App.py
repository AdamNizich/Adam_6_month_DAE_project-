

# Mets Win Prediction App

print("Welcome to the Mets Win Prediction App!")

while True:

    print("\n--- Enter Mets Players Information ---")

    mets_player1 = input("Enter Mets player 1 name: ")
    mets_rank1 = int(input("Enter player 1 ranking (1-100): "))

    mets_player2 = input("Enter Mets player 2 name: ")
    mets_rank2 = int(input("Enter player 2 ranking (1-100): "))

    mets_average = (mets_rank1 + mets_rank2) / 2

    print("\n--- Enter Opponent Players Information ---")

    opp_player1 = input("Enter opponent player 1 name: ")
    opp_rank1 = int(input("Enter opponent player 1 ranking (1-100): "))

    opp_player2 = input("Enter opponent player 2 name: ")
    opp_rank2 = int(input("Enter opponent player 2 ranking (1-100): "))

    opp_average = (opp_rank1 + opp_rank2) / 2

    print("\n--- Results ---")
    print("Mets average rating:", mets_average)
    print("Opponent average rating:", opp_average)

    if mets_average > opp_average:
        print("Prediction: Mets Win!")
    elif opp_average > mets_average:
        print("Prediction: Opponent Wins!")
    else:
        print("Prediction: It's a tie!")

    predict_again = input("\nPredict again? (yes/no): ").lower()

    if predict_again != "yes":
        break

print("Program Ended.")