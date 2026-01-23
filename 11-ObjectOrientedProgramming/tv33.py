class TV:
    def __init__(self):
        self.is_on = False      # TV is initially off
        self.channel_no = 1     # TV initially set to channel 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no  # update the channel number

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
