from tv36 import TV

def main():
    # Create TV set
    my_tv = TV()
    
    # Show initial status
    my_tv.show_status()
    
    # Turn TV on
    my_tv.turn_on()
    my_tv.show_status()
    
    # Set channels
    channels_list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "HBO"]
    my_tv.set_channels(channels_list)
    
    # Change channels and show status
    my_tv.set_channel(4)
    my_tv.show_status()
    
    # Increase volume
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.show_status()
    
    # Decrease volume
    my_tv.decrease_volume()
    my_tv.show_status()
    
    # Try to exceed volume limits
    for x in range(15):
        my_tv.increase_volume()
    my_tv.show_status()
    
    for x in range(15):
        my_tv.decrease_volume()
    my_tv.show_status()
    
    # Turn TV off
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
