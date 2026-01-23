from tv33 import TV

def main():
    my_tv = TV()  # create TV set

    print("Show TV status:")
    my_tv.show_status()  # TV is off

    print("\nTurn TV on:")
    my_tv.turn_on()
    my_tv.show_status()  # TV is on, channel 1

    print("\nChange TV channel to 5:")
    my_tv.set_channel(5)
    my_tv.show_status()  # TV is on, channel 5

    print("\nTurn TV off:")
    my_tv.turn_off()
    my_tv.show_status()  # TV is off

if __name__ == "__main__":
    main()
