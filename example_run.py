import time
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, \
    SensorBridgeShdlcDevice, SensorBridgeI2cProxy
from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_sdp import SdpI2cDevice

# Connect to the SensorBridge with default settings:
#  - baudrate:      460800
#  - slave address: 0
with ShdlcSerialPort(port='COM1', baudrate=460800) as port:
    bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    print("SensorBridge SN: {}".format(bridge.get_serial_number()))

    # Configure SensorBridge port 1 for SDP
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create SDP device
    #
    # Make sure to use the correct i2c address:
    # SDP8xx supports the 0x25 and 0x26 I²C addresses, SDP3x supports the
    # 0x21, 0x22 and 0x23 I²C addresses.
    # Refer to the dedicated datahseet for more detailed information.
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    sdp = SdpI2cDevice(I2cConnection(i2c_transceiver), slave_address=0x25)
    sdp.stop_continuous_measurement()
    sdp.start_continuous_measurement_with_mass_flow_t_comp()

    # Measure
    try:
        for _ in range(50):
            differential_pressure, temperature = sdp.read_measurement()
            # use default formatting for printing output:
            print("{}, {}".format(differential_pressure, temperature))
            # custom printing of attributes:
            print("{:0.2f} °C ({} ticks), {:0.2f} Pa ({} ticks)".format(
                temperature.degrees_celsius, temperature.ticks,
                differential_pressure.pascal, differential_pressure.ticks))
            time.sleep(0.2)
    finally:
        sdp.stop_continuous_measurement()
        bridge.switch_supply_off(SensorBridgePort.ONE)
