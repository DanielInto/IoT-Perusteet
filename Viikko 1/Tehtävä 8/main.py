import network
import time
import urequests
import dht
from machine import Pin

ssid = 'Wokwi-GUEST'
password = ''

THINGSPEAK_API_KEY = 'HGIOEEw8512YQMD'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("Connecting to WiFi...", end="")
wlan.connect(ssid, password)

while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\nConnected to WiFi!")
print("IP address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(15))

def send_to_thingspeak(temp):
    try:
        response = urequests.post(
            THINGSPEAK_URL,
            data='api_key={}&field1={}'.format(THINGSPEAK_API_KEY, temp),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("Data sent! Response:", response.text)
        response.close()
    except Exception as e:
        print("Error sending data:", e)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        print("Temperature:", temp, "°C")
        send_to_thingspeak(temp)
    except Exception as e:
        print("Sensor read error:", e)
    time.sleep(15)
