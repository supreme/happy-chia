"""
the_joy_of_watering.py

Created by Stephen Andrews, February 21st, 2020.
"""
import time

from bob.sensors.scale import Scale


class TheJoyOfWatering:

    # Load cell pin config
    LC_DT_PIN = 20
    LC_SCK_PIN = 21

    def __init__(self):
        self.scale = Scale(self.LC_DT_PIN, self.LC_SCK_PIN)

    def run(self):
        while True:
            print(f'Weight {self.scale.get_weight()}g')
            time.sleep(1)



if __name__ == '__main__':
    with TheJoyOfWatering() as bob:
        bob.run()
