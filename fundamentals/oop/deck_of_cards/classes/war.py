import classes.card

def playWar(p1, p2):
    p1_points = 0
    p2_points = 0
    for card in range(len(p1.hand)):
        if p1.hand[card].point_val > p2.hand[card].point_val:
            p1_points += 1
            print(f"Player 1 attacks: {p1.hand[card]}")
            print(f"Player 2 attacks: {p2.hand[card]}")
            print("Player 1 won this battle!")
        elif p1.hand[card].point_val == p2.hand[card].point_val:
            print(f"Player 1 attacks: {p1.hand[card]}")
            print(f"Player 2 attacks: {p2.hand[card]}")
            print("DRAW!")
        else: 
            p2_points += 1
            print(p1.hand[card])
            print(p2.hand[card])
            print("Player 2 won this battle!")
    if p1_points > p2_points:
        print("Player 1 has won the war!")
    elif p1_points == p2_points:
        print("DRAW!")
    else:
        print("Player 2 has won the war!")