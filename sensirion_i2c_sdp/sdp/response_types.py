# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function


class SdpTemperature(object):
    """
    Represents a measurement response for the temperature.

    With the :py:attr:`ticks` you can access the raw data as received from the
    device. For the converted values you can choose between
    :py:attr:`degrees_celsius` and :py:attr:`degrees_fahrenheit`.

    :param int ticks:
        The read ticks as received from the device.
    """

    def __init__(self, ticks):
        """
        Creates an instance from the received raw data.
        """

        #: The ticks (int) as received from the device.
        self.ticks = ticks

        #: The converted temperature in °C.
        self.degrees_celsius = float(ticks) / 200.

        #: The converted temperature in °F.
        self.degrees_fahrenheit = (ticks * 9. / 1000.) + 32

    def __str__(self):
        return '{:0.1f} °C'.format(self.degrees_celsius)


class SdpDifferentialPressure(object):
    """
    Represents a measurement response for the differential pressure.

    With the :py:attr:`ticks` you can access the raw data as received from the
    device. For the converted value the :py:attr:`pascal` attribute is
    available.

    :param int ticks:
        The read ticks as received from the device.
    :param int scale_factor:
        The read scaling factor to convert the received differential pressure
        ticks as received from the sensor into Pascal.
    """

    def __init__(self, ticks, scale_factor):
        """
        Creates an instance from the received raw data.
        """

        #: The ticks (int) as received from the device.
        self.ticks = ticks

        #: The scale factor (int) as received from the device.
        self.scale_factor = scale_factor

        #: The converted concentration in vol%.
        self.pascal = float(self.ticks) / float(self.scale_factor)

    def __str__(self):
        return '{:0.2f} Pa'.format(self.pascal)
