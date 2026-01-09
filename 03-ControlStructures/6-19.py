###
# Yes-no survey with logical variables
#

print("SURVEY")


interested_in_cs = input("Are you interested in computer science? (y/n): ").lower() == 'y'
likes_games = input("Do you like playing computer games? (y/n): ").lower() == 'y'
has_instagram = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if interested_in_cs else 'No'}")
print(f"Playing computer games: {'Yes' if likes_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram else 'No'}")
