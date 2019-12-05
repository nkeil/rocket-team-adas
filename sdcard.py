import board
import busio
import digitalio
import adafruit_sdcard
import storage

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Use board.SD_CS for Feather M0 Adalogger
cs = digitalio.DigitalInOut(board.SD_CS)
# Or use a GPIO pin like 15 for ESP8266 wiring:
#cs = digitalio.DigitalInOut(board.GPIO15)

sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

storage.mount(vfs, "/test_root")