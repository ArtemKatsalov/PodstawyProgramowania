###
# EAN-13 barcode checker
#

ean = input("Enter EAN-13 article number: ")

# Sprawdzenie, czy numer składa się dokładnie z 13 cyfr
if len(ean) == 13 and ean.isdigit():
    print("The article number is correct")
    
    # Sprawdzenie, czy numer zaczyna się od 590 (Polska)
    if ean[:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Invalid article number")
