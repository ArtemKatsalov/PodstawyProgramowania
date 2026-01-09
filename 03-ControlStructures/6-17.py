time_24 = input("Enter time (24-hour format hh:mm): ")

hh = int(time_24[0:2])
mm = int(time_24[3:5])

if hh == 0:
    print(f"Time in 12-hour format: 12:{mm:02d}am")
elif 1 <= hh < 12:
    print(f"'Time in 12-hour format:{hh}:{mm:02d}am")
elif hh == 12:
    print(f"Time in 12-hour format: 12:{mm:02d}pm")
else:
    print(f"Time in 12-hour format: {hh-12}:{mm:02d}pm")