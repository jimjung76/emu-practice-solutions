def pirateLoot(coins, pirates):
    numPirates = pirates
    while pirates > 0:
        share = (coins%numPirates) + int(coins/numPirates)
        print(share)
        coins = coins - share
        pirates -= 1
    print(coins)


