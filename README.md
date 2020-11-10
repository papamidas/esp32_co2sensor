# esp32_co2sensor
CO2-Sensor with VZ89-TE and WIFIKIT32

- Install Thonny, preferably v3.3.0b7 or newer from here: https://github.com/thonny/thonny/releases/tag/v3.3.0b7
- Download “esp32-idf4-20200902-v1.13.bin” or newer micropython firmware version from here: https://micropython.org/download/esp32/
- Flash your WIFI KIT 32 with Thonny (Tools->Options->Interpreter->Micropython(ESP32)->Open the dialog for installing or upgrading Micropython on your device)
- Clone repository https://github.com/micropython/micropython or copy/download at least "ssd1306.py" from https://github.com/micropython/micropython/tree/master/drivers/display
- Clone this repository or download "main.py" and VZ89TE.py from this repository
- Read data sheet of VZ89TE: https://www.sgxsensortech.com/content/uploads/2016/07/MiCS-VZ-89TE-V1.0.pdf
- Also worth reading: https://www.sgxsensortech.com/content/uploads/2017/03/I2C-Datasheet-MiCS-VZ-89TE-rev-H-ed170214-Read-Only.pdf
- Also worth reading: https://www.sgxsensortech.com/content/uploads/2016/07/Customer-upgrade-guide-MiCS-VZ89TD-to-MiCS-VZ89TE.pdf
- Connect pin 2 (SCL) of sensor VZ89TE to pin 22 of WIFI KIT 32
- Connect pin 4 (SDA) of sensor VZ89TE to to pin 21 of WIFI KIT 32
- Connect pin 6 of sensor to 3.3V of WIFI KIT 32 and pin 3 to GND
- Do not forget to connect 2 x 4k7 resistors from SDA,SCL to 3.3V
- Connect cathode of an LED to pin 19 of WIFI KIT and anode via a resistor (1k or so) to 3.3V. Useful for determining if program is running
- The WIFI KIT 32 Pinout can be found here https://resource.heltec.cn/download/WiFi_Kit_32/WIFI_Kit_32_pinoutDiagram_V2.pdf
- Beware: there seem to exist WIFI KIT 32 versions with a mirrored pinout!
- A picture of the setup can be found here: https://dm1cr.de/co2-sensor-gegen-corona-version-mit-wifi-kit-32-und-sgx-sensortech-mics-vz89te-und-micropython
   
