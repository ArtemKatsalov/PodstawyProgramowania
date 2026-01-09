# card_mask.py
def hide(card_number):
    return card_number[:2] + "*" * (len(card_number) - 6) + card_number[-4:]
