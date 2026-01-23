from tv34 import TV

def main():
    # Create TV set
    my_tv = TV()
    
    # Show initial status
    my_tv.show_status()
    
    # Turn TV on
    my_tv.turn_on()
    my_tv.show_status()
    
    # Display channels (none yet)
    my_tv.show_channels()
    
    # Set channels
    channels_list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    my_tv.set_channels(channels_list)
    
    # Display channels again
    my_tv.show_channels()
    
    # Show TV status again
    my_tv.show_status()
    
    # Turn TV off
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
