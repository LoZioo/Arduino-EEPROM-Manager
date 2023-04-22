# Arduino-EEPROM-Manager
A little firmware and a Python tool to allow flashing of binaries directly into the EEPROM of microcontrollers that support the EEPROM.h library from the Arduino framework.

## Usage
1.	Use [PlatformIO](https://platformio.org/) to compile and flash the firmware for your specific architecture (check the [platformio.ini](src/EEPROM_Manager/platformio.ini) file).

2.	Install the latest Python 3.11 (I'd suggest using [pyenv](https://github.com/pyenv/pyenv) just to not mess up with your system Python installation).
3.	Get a shell and cd to the `src/EEPROM_Manager` folder.
4.	Type `pip install -r requirements.txt` to install the needed dependencies.
5.	Finally, type `python eeprom-tool.py` to display the help screen.

## License
[The MIT License](LICENSE)
