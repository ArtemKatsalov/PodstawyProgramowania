class TV:
    def __init__(self):
        self.is_on = False          # TV initially off
        self.channel_no = 1         # TV initially set to channel 1
        self.channels = []          # initially no channels available
        self.volume = 0             # initial volume level

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            # Display channel number and name
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({channel_name}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no} (no name), volume {self.volume}")
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        if new_channel_no > 0:
            self.channel_no = new_channel_no
        else:
            print("Invalid channel number!")

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if not self.channels:
            print("No channels available.")
        else:
            print("Channel list:")
            for i, channel in enumerate(self.channels, start=1):
                print(f"{i}. {channel}")

    # Volume control methods
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume is already at maximum (10).")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is already at minimum (0).")
