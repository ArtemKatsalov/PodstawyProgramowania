from tv import TV

def main():
    # object creation
    my_tv = TV()

    # object usage
    print("Create TV set")
    my_tv.show_status()

    print("Turn TV on")
    my_tv.turn_on()
    my_tv.show_status()

    print("Turn TV off")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
