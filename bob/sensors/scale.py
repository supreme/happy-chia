"""
scale.py

Created by Stephen Andrews, February 21st, 2020.
"""
import RPi.GPIO as GPIO

from bob.sensors.hx711 import HX711


class Scale:
    """A more conveniant API around the HX711 library."""

    # The reference unit for the load cell
    REFERENCE_UNIT = 376.6

    def __init__(self, dt_pin, sck_pin):
        """
        Creates a new scale instance.

        :param dt_pin: The DT pin of the HX711
        :param sck_pin: The SCK pin of the HX711
        """
        self.hx = HX711(dt_pin, sck_pin)

        self.hx.set_reading_format("MSB", "MSB")
        self.hx.set_reference_unit(self.REFERENCE_UNIT)
        self.hx.reset()
        self.hx.tare()

    def get_weight(self, measurements=5):
        return self.hx.get_weight(measurements)
