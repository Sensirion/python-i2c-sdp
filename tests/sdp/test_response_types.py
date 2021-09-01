# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest

from sensirion_i2c_sdp.sdp.response_types import SdpDifferentialPressure, SdpTemperature


@pytest.mark.parametrize("value", [
    dict({'ticks': 60, 'pascal': 1., 'scale_factor': 60}),
    dict({'ticks': 0, 'pascal': 0., 'scale_factor': 60}),
    dict({'ticks': -90, 'pascal': -1.5, 'scale_factor': 60}),
])
def test_differential_pressure(value):
    """
    Test if the SdpDifferentialPressure() type works as expected for different
    values.
    """
    result = SdpDifferentialPressure(value.get('ticks'), value.get('scale_factor'))
    assert type(result) is SdpDifferentialPressure
    assert type(result.ticks) is int
    assert result.ticks == value.get('ticks')
    assert type(result.pascal) is float
    assert result.pascal == pytest.approx(value.get('pascal'), 0.01)


@pytest.mark.parametrize("value", [
    dict({'ticks': 0, 'degrees_celsius': 0., 'degrees_fahrenheit': 32.}),
    dict(
        {'ticks': 20000, 'degrees_celsius': 100., 'degrees_fahrenheit': 212.}),
    dict(
        {'ticks': -5000, 'degrees_celsius': -25., 'degrees_fahrenheit': -13.}),
])
def test_temperature(value):
    """
    Test if the SdpTemperature() type works as expected for different values.
    """
    result = SdpTemperature(value.get('ticks'))
    assert type(result) is SdpTemperature
    assert type(result.ticks) is int
    assert result.ticks == value.get('ticks')
    assert type(result.degrees_celsius) is float
    assert result.degrees_celsius == value.get('degrees_celsius')
    assert type(result.degrees_fahrenheit) is float
    assert result.degrees_fahrenheit == value.get('degrees_fahrenheit')
