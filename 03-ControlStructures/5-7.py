# timer.py - countdown timer with last 5 seconds in words
import time

N = int(input("Enter the number of seconds to count down: "))

number_words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}

while N > 0:
    if N in number_words:
        print(number_words[N])
    else:
        print(N)
    time.sleep(1)  
    N -= 1

print("Time's up!")
