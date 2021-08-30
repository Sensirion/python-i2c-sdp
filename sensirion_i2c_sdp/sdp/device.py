# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

from sensirion_i2c_driver import I2cDevice

from sensirion_i2c_sdp.sdp.commands import SdpI2cCmdPrepareProductIdentifier, SdpI2cCmdReadProductIdentifier, \
    SdpI2cCmdStartContinuousMeasurementWithMassFlowTCompAndAveraging, SdpI2cCmdStopContinuousMeasurement, \
    SdpI2cCmdReadMeasurement, SdpI2cCmdStartContinuousMeasurementWithMassFlowTComp, \
    SdpI2cCmdStartContinuousMeasurementWithDiffPressureTCompAndAveraging, \
    SdpI2cCmdStartContinuousMeasurementWithDiffPressureTComp, \
    SdpI2cCmdTriggerMeasurementWithMassFlowTCompAndAveraging, SdpI2cCmdTriggerMeasurementWithDiffPressureTComp, \
    SdpI2cCmdEnterSleepMode, SdpI2cCmdExitSleepMode


class SdpI2cDevice(I2cDevice):
    """
    SDP I²C device class to allow executing I²C commands.

    Adjust the I2C address according to your setup.

    SDP8xx can support 0x25 and 0x26.
    SDP3x can support 0x21, 0x22 and 0x23.

    Please refer to the dedicated Datasheet for more details on the supported I2C address range.
    """

    def __init__(self, connection, slave_address=0x25):
        """
        Constructs a new SDP I²C device.

        :param ~sensirion_i2c_driver.connection.I2cConnection connection:
            The I²C connection to use for communication.
        :param byte slave_address:
            The I²C slave address, defaults to 0x25.
        """
        super().__init__(connection, slave_address)

    def read_product_identifier(self):
        """
        Read the product identifier and serial number of the sensor.

        :return: The product number and serial number.
        :rtype: tuple
        """
        self.execute(SdpI2cCmdPrepareProductIdentifier())
        return self.execute(SdpI2cCmdReadProductIdentifier())

    def start_continuous_measurement_with_mass_flow_t_comp_and_averaging(self):
        """
        This command starts continuous measurements with mass flow temperature
        compensation and the average till read feature.

        .. note:: The measurement command must only be sent once, if acknowledged.
                  The command must not be resent or other commands must not be sent
                  until the stop measurement command has been issued. After the
                  start measurement command is sent, the first measurement result
                  is available after 8ms. Small accuracy deviations (few % of
                  reading) can occur during the next 12ms. The measured values are
                  updated every 0.5ms and can be read using the read measurement
                  interface.
        """
        return self.execute(SdpI2cCmdStartContinuousMeasurementWithMassFlowTCompAndAveraging())

    def start_continuous_measurement_with_mass_flow_t_comp(self):
        """
        This command starts continuous measurements with mass flow temperature
        compensation.

        .. note:: The measurement command must only be sent once, if acknowledged.
                  The command must not be resent or other commands must not be sent
                  until the stop measurement command has been issued. After the
                  start measurement command is sent, the first measurement result
                  is available after 8ms. Small accuracy deviations (few % of
                  reading) can occur during the next 12ms. The measured values are
                  updated every 0.5ms and can be read using the read measurement
                  interface.
        """
        return self.execute(SdpI2cCmdStartContinuousMeasurementWithMassFlowTComp())

    def start_continuous_measurement_with_diff_pressure_t_comp_and_averaging(self):
        """
        This command starts continuous measurements with differential pressure
        temperature compensation and the average till read feature.

        .. note:: The measurement command must only be sent once, if acknowledged.
                  The command must not be resent or other commands must not be sent
                  until the stop measurement command has been issued. After the
                  start measurement command is sent, the first measurement result
                  is available after 8ms. Small accuracy deviations (few % of
                  reading) can occur during the next 12ms. The measured values are
                  updated every 0.5ms and can be read using the read measurement
                  interface.
        """
        return self.execute(SdpI2cCmdStartContinuousMeasurementWithDiffPressureTCompAndAveraging())

    def start_continuous_measurement_with_diff_pressure_t_comp(self):
        """
        This command starts continuous measurements with differential pressure
        temperature compensation.

        .. note:: The measurement command must only be sent once, if acknowledged.
                  The command must not be resent or other commands must not be sent
                  until the stop measurement command has been issued. After the
                  start measurement command is sent, the first measurement result
                  is available after 8ms. Small accuracy deviations (few % of
                  reading) can occur during the next 12ms. The measured values are
                  updated every 0.5ms and can be read using the read measurement
                  interface.
        """
        return self.execute(SdpI2cCmdStartContinuousMeasurementWithDiffPressureTComp())

    def trigger_measurement_with_mass_flow_t_comp_and_averaging(self):
        """
        This command triggers a single shot measurement with mass flow temperature
        compensation.

        .. note:: During a triggered measurement the sensor measures both
                  differential pressure and temperature. The measurement starts
                  directly after the command has been sent. The command needs to be
                  repeated with every measurement. During the 45ms that the sensor
                  is measuring, no command can be sent to the sensor. After the
                  45ms the result can be read out and any command can be sent to
                  the sensor.
        """
        return self.execute(SdpI2cCmdTriggerMeasurementWithMassFlowTCompAndAveraging())

    def trigger_measurement_with_diff_pressure_t_comp_and_averaging(self):
        """
        This command triggers a single shot measurement with differential pressure
        temperature compensation.

        .. note:: During a triggered measurement the sensor measures both
                  differential pressure and temperature. The measurement starts
                  directly after the command has been sent. The command needs to be
                  repeated with every measurement. During the 45ms that the sensor
                  is measuring, no command can be sent to the sensor. After the
                  45ms the result can be read out and any command can be sent to
                  the sensor.
        """
        return self.execute(SdpI2cCmdTriggerMeasurementWithDiffPressureTComp())

    def stop_continuous_measurement(self):
        """
        This command stops the continuous measurement and puts the sensor in idle
        mode. It powers off the heater and makes the sensor receptive to another
        command after 500us. The Stop command is also required when switching
        between different continuous measurement commands.
        """
        return self.execute(SdpI2cCmdStopContinuousMeasurement())

    def read_measurement(self):
        """
        Read Measurement from sensor.

        After a start continuous measurement commands, the measurement results can
        be read out at most every 0.5ms. After a triggered measurement command, the
        results can be read out when the sensor is finished with the measurement.

        :return:
            - differential_pressure (:py:class:sensirion_i2c_sdp.sdp.response_types.SdpDifferentialPressure)
              Differential Pressure response object
            - temperature (:py:class:sensirion_i2c_sdp.sdp.reasponse_types.SdpTemperature)
              Temperature response object.
        :rtype: tuple
        """
        return self.execute(SdpI2cCmdReadMeasurement())

    def enter_sleep_mode(self):
        """
        In sleep mode the sensor uses the minimum amount of current. The mode can
        only be entered from idle mode, i.e. when the sensor is not measuring. This
        mode is particularly useful for battery operated devices. To minimize the
        current in this mode, the complexity of the sleep mode circuit has been
        reduced as much as possible, which is mainly reflected by the way the
        sensor exits the sleep mode. In sleep mode the sensor cannot be soft reset.

        .. note:: Triggered mode: the sleep command can be sent after the result
                  have been read out and the sensor is in idle mode. Continuous
                  mode: the sleep command can be sent after a stop continuous
                  measurement command has been issued and the sensor is in idle
                  mode.
        """
        self.execute(SdpI2cCmdEnterSleepMode())

    def exit_sleep_mode(self):
        """
        Exit sleep mode. See the data sheet for more detailed information
        """
        self.execute(SdpI2cCmdExitSleepMode())
