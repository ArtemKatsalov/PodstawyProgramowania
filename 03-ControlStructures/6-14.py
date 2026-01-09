###
# Influencer checker using logical variables
#

facebook = True
twitter = False
instagram = True

# Sprawdzenie, czy osoba ma co najmniej dwa konta
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")
