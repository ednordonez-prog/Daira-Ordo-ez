import random

game_count = 0  # counts how many games are played

# Build a complete deck of 52 cards
def create_deck():
    deck = []
    values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    for v in values:
        for i in range(4):
            deck.append(v)
    return deck

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Draw the top card
def deal_card(deck):
    return deck.pop()

# Calculate hand total and fix aces
def calculate_total(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

# Deal two cards to player and dealer
def initial_deal(deck):
    player = [deal_card(deck), deal_card(deck)]
    dealer = [deal_card(deck), deal_card(deck)]
    return player, dealer

# Player turn (SCAM IS HERE)
def player_turn(deck, player):
    global game_count
    scam_round = (game_count % 5 == 0)

    while True:
        total = calculate_total(player)
        print("Your hand:", player, "Total:", total)

        if total > 21:
            print("You bust!")
            return player

        choice = input("Hit or stand? (h/s): ").lower()
        if choice == "h":
            if scam_round and total == 16:
                player.append(10)   # rigged bad card
            else:
                player.append(deal_card(deck))
        else:
            return player

# Dealer draws until 17+
def dealer_turn(deck, dealer):
    while calculate_total(dealer) < 17:
        dealer.append(deal_card(deck))
    return dealer

# Compare totals and print result
def determine_winner(player, dealer):
    p = calculate_total(player)
    d = calculate_total(dealer)

    print("\nFinal totals → You:", p, "Dealer:", d)

    if p > 21:
        print("Dealer wins!")
    elif d > 21:
        print("You win!")
    elif p > d:
        print("You win!")
    elif d > p:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run one game
def main():
    global game_count
    game_count += 1

    print("\nGame", game_count)

    deck = create_deck()
    shuffle_deck(deck)

    player, dealer = initial_deal(deck)

    print("Dealer shows:", dealer[0])

    player = player_turn(deck, player)

    if calculate_total(player) <= 21:
        dealer = dealer_turn(deck, dealer)
        print("Dealer hand:", dealer)

    determine_winner(player, dealer)

# Play again loop
while True:
    main()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break

