from VZ89TE import VZ89TE
from ssd1306 import SSD1306_I2C
import utime
from machine import Pin, I2C

def mapvalue(x, in_min, in_max, out_min, out_max):
    if (x > in_max):
        x = inmax
    if (x < in_min):
        x = in_min
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

led = Pin(19, Pin.OUT)
led.on()

# Pin 16 is SSD1306 Display Enable
pin16 = Pin(16, Pin.OUT)
pin16.on()
displayi2c = I2C(scl=Pin(15), sda=Pin(4))
display = SSD1306_I2C(128, 64, displayi2c)
display.fill(0)

sensori2c = I2C(1,scl=Pin(22), sda=Pin(21), freq = 100000)
sensor = VZ89TE(sensori2c)

print("Display Width: ", display.width)
print("Display Height: ", display.height)

print("I2C slave found at adr ", hex(sensori2c.scan()[0]) )
print("Revision: ", sensor.getRevision())
print("Year: ", sensor.getRevision()["Year"])
print("Month: ", sensor.getRevision()["Month"])
print("Day: ", sensor.getRevision()["Day"])

CO2DISPMAX = 1000
CO2DISPMIN = 400
co2 = 0

while True:

    try:

        co2 = sensor.getData()["CO2"]
        
    except ValueError:
    
        co2 = co2
    
    display.fill(0)
    w = int(mapvalue(co2, CO2DISPMIN, 1000, 0, display.width))
    display.rect(0,0, display.width, display.height-12, 1)
    display.fill_rect(0, 0, w, display.height-1-12, 1)
    display.text("CO2: " + str(int(co2)) + " ppm", 0, display.height-1-8)
    display.show()

    try:

         print(sensor.getData())

    except ValueError:

         print("oops! crc error!")

    led.off()
    utime.sleep_ms(500)
    led.on()
    utime.sleep(2)
