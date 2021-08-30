# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest
from sensirion_i2c_driver.errors import I2cNackError

from sensirion_i2c_sdp.sdp.response_types import SdpDifferentialPressure, SdpTemperature


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_product_identifier(sdp):
    product_number, serial_number = sdp.read_product_identifier()
    assert type(product_number) is int
    assert type(serial_number) is int
    assert serial_number > 1e9


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_measurement_continuous_1(sdp):
    sdp.start_continuous_measurement_with_diff_pressure_t_comp_and_averaging()
    dp, temperature = sdp.read_measurement()
    assert_measurement_result(dp, temperature)
    sdp.stop_continuous_measurement()


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_measurement_continuous_2(sdp):
    sdp.start_continuous_measurement_with_diff_pressure_t_comp()
    dp, temperature = sdp.read_measurement()
    assert_measurement_result(dp, temperature)
    sdp.stop_continuous_measurement()


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_measurement_continuous_3(sdp):
    sdp.start_continuous_measurement_with_mass_flow_t_comp_and_averaging()
    dp, temperature = sdp.read_measurement()
    assert_measurement_result(dp, temperature)
    sdp.stop_continuous_measurement()


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_measurement_continuous_4(sdp):
    sdp.start_continuous_measurement_with_mass_flow_t_comp_and_averaging()
    dp, temperature = sdp.read_measurement()
    assert_measurement_result(dp, temperature)
    sdp.stop_continuous_measurement()


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_measurement_single_shot_1(sdp):
    sdp.trigger_measurement_with_diff_pressure_t_comp_and_averaging()
    dp, temperature = sdp.read_measurement()
    assert_measurement_result(dp, temperature)


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_read_measurement_single_shot_2(sdp):
    sdp.trigger_measurement_with_mass_flow_t_comp_and_averaging()
    dp, temperature = sdp.read_measurement()
    assert_measurement_result(dp, temperature)


def assert_measurement_result(dp, temperature):
    assert type(dp) is SdpDifferentialPressure
    assert type(dp.ticks) is int
    assert type(dp.pascal) is float
    assert type(dp.scale_factor) is int
    assert type(temperature) is SdpTemperature
    assert temperature.degrees_celsius is not None


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_sleep_mode_should_be_sleeping(sdp):
    sdp.enter_sleep_mode()

    # Sensor should be sleeping
    with pytest.raises(I2cNackError):
        sdp.trigger_measurement_with_mass_flow_t_comp_and_averaging()

    # Any write header wakes up the sensor... hence now no NACK is expected
    sdp.trigger_measurement_with_mass_flow_t_comp_and_averaging()


@pytest.mark.needs_device
@pytest.mark.needs_sdp
def test_sleep_mode_should_wake_up(sdp):
    sdp.enter_sleep_mode()
    with pytest.raises(I2cNackError):
        sdp.exit_sleep_mode()

    # exit_sleep_mode should wake up the sensor... hence now no NACK is expected
    sdp.trigger_measurement_with_mass_flow_t_comp_and_averaging()
