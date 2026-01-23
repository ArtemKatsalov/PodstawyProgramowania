from thermometer import Thermometer

def main():
    # Create a thermometer object
    my_thermometer = Thermometer()

    # Turn thermometer on
    my_thermometer.turn_on()

    # Measure temperature
    my_thermometer.measure_temperature()

    # Display temperature
    my_thermometer.display_temperature()

    # Turn thermometer off
    my_thermometer.turn_off()

if __name__ == "__main__":
    main()
