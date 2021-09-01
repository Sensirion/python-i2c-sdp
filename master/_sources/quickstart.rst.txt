Quick Start
===========

SensorBridge Example
--------------------

Following example code shows how to use this driver with a Sensirion SDP8xx
connected to the computer using a `Sensirion SEK-SensorBridge`_. It is assumed,
that the sensor is plugged into port 1 of the SensorBridge and COM Port 1 is
used on the computer. The driver for the SensorBridge can be installed with

.. sourcecode:: bash

    pip install sensirion-shdlc-sensorbridge

Depending on the sensor type you connect set the I2C address accordingly when
creating the SdpI2cDevice instance. For more details see comments in the code.

.. literalinclude:: ../example_run.py
   :language: python

.. _Sensirion SEK-SensorBridge: https://www.sensirion.com/sensorbridge/
