# Python Driver for Sensirion I²C SDP8xx and SDP3x Sensors

This repository contains the Python driver to communicate with Sensirion SDP8xx
and SDP3x sensors using the I²C interface. For details, please read the package
description in [README.rst](README.rst).

## Supported Sensors

* **SDP8xx:** Differential pressure sensors of the SDP800 series are the
  reliable solution for precise air flow measurement in most demanding but
  cost-sensitive HVAC applications, such as VAV controllers, burners, heat
  recovery systems and filter monitoring.
* **SDP3x:** The SDP3x is the world's smallest differential pressure sensor. It
  measures just 5 mm x 8 mm x 5 mm, opening up new dimensions of integration
  and application possibilities. The sensor is based on the next generation of
  the CMOSens® sensor chip and is the heart of Sensirion's new sensor platform
  for measuring differential pressure and mass flow.

## Usage

See package description in [README.rst](README.rst) and user manual at
[https://sensirion.github.io/python-i2c-sdp/](https://sensirion.github.io/python-i2c-sdp/)
.

## Development

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

### Run tests

Unit tests can be run with [`pytest`](https://pytest.org/):

```bash
pip install -e .[test]                             # Install requirements
pytest -m "not needs_device"                       # Run tests without hardware
pytest                                             # Run all tests
pytest -m "not (needs_device and not needs_sdp)"   # Run all tests for sdp
```

The tests with the marker `needs_sdp` have following requirements:

- An SDP device must be connected to a
  [SensorBridge](https://www.sensirion.com/sensorbridge/) on port 1.
- Pass the serial port where the SensorBridge is connected with
  `--serial-port`, e.g. `pytest --serial-port=COM7`
- The SensorBridge must have default settings (baudrate 460800, address 0)

### Build documentation

The documentation can be built with [Sphinx](http://www.sphinx-doc.org/):

```bash
python setup.py install                        # Install package
pip install -r docs/requirements.txt           # Install requirements
sphinx-versioning build docs docs/_build/html  # Build documentation
```

## License

See [LICENSE](LICENSE).
