from tv35 import TV

def main():
    # Create TV set
    my_tv = TV()
    
    # Show initial status
    my_tv.show_status()
    
    # Turn TV on
    my_tv.turn_on()
    my_tv.show_status()
    
    # Set 7 channels
    channels_list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "HBO"]
    my_tv.set_channels(channels_list)
    
    # Show channels
    my_tv.show_channels()
    
    # Change channel numbers and print status
    my_tv.set_channel(1)
    my_tv.show_status()
    
    my_tv.set_channel(4)
    my_tv.show_status()
    
    my_tv.set_channel(7)
    my_tv.show_status()
    
    my_tv.set_channel(8)  # exceeds available channels
    my_tv.show_status()
    
    # Turn TV off
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
