import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None  # measured temperature

    def turn_on(self):
        self.is_on = True
        print("Thermometer is ON.")

    def turn_off(self):
        self.is_on = False
        print("Thermometer is OFF.")

    def measure_temperature(self):
        if self.is_on:
            # generate a random temperature from 34.0 to 42.0 with 0.1 precision
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Cannot measure: Thermometer is OFF.")

    def display_temperature(self):
        if self.temperature is None:
            print("No temperature measured yet.")
        else:
            msg = f"Temperature: {self.temperature}C"
            
            # check for fever
            if 37.0 <= self.temperature < 41.0:
                msg += " (fever)"
            elif self.temperature >= 41.0:
                msg += " (CRITICAL TEMPERATURE!!)"
            
            print(msg)
