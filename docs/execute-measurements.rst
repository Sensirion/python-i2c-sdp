Install the SDP Driver
--------------------------

.. include:: driver-installation.rst


Use the SensorBridge on Windows
-------------------------------

1. Install the driver for the `Sensirion SEK-SensorBridge`_:

   .. code-block:: console

      python -m pip install sensirion-shdlc-sensorbridge

2. Connect the SEK-SensorBridge to your PC over USB.

   If the SEK-SensorBridge is not detected by your system, follow the
   `SensorBridge FTDI Driver Installation`_.

3. Connect the SDP sensor to the SEK-SensorBridge.

4. Run an example script in the activated virtual environment.

   By default, the script assumes that the SensorBridge is connected to the
   ``COM1`` serial port. If a different port is used, specify it with the
   ``--serial-port`` parameter:

   .. code-block:: console

        python example_run.py --serial-port <your COM port>


.. _Sensirion SEK-SensorBridge: https://developer.sensirion.com/product-support/sek-sensorbridge/
.. _SensorBridge FTDI Driver Installation: https://sensirion.github.io/python-shdlc-sensorbridge/sensor-bridge-installation.html

Example script
~~~~~~~~~~~~~~

.. literalinclude:: ../example_run.py
    :language: python
