def f(dice):
    if not dice:              # check if the string is empty
        return 0

    max_streak = 1            # maximum streak length
    current_streak = 1        # current streak length
    prev_digit = dice[0]      # previous digit to compare

    for digit in dice[1:]:
        if digit == prev_digit:           # same as previous?
            current_streak += 1          # increment current streak
            max_streak = max(max_streak, current_streak)  # update max streak if needed
        else:
            current_streak = 1           # reset streak
            prev_digit = digit           # update previous digit

    return max_streak

# Test examples
print(f("5233165554211"))  # 5?  3
print(f("2133"))           # 3?  2
