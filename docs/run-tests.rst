Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install test requirements


Connect your SPD sensor to a
`SensorBridge <https://sensirion.com/products/catalog/SEK-SensorBridge/>`_ on port 1. Assuming the SensorBridge is
attached to COM1 you can start the tests with the following command:

.. code-block:: bash

    pytest --serial-port=COM1                    # Run all tests for SPD on the sensor attached to COM1


.. note::
    The SensorBridge must have default settings (baudrate 460800, address 0)

In order to select tests for only SDP, you can use the ``-m`` option of pytest:

.. code-block:: bash

    pytest -m "not (needs_device and not needs_sdp)"   # Run all tests for sdp

