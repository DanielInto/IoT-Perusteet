from machine import Pin
import time


pir = Pin(28, Pin.IN)
print("PIR ready. Monitoring for motion...")

alarm_active = False
alarm_duration = 10 

last_motion_time = 0

while True:
    if pir.value() == 1:
        last_motion_time = time.time()
        if not alarm_active:
            alarm_active = True
            print("MOTION DETECTED! Alarm active.")

    if alarm_active:
        if time.time() - last_motion_time > alarm_duration:
            alarm_active = False
            print("All clear — no motion detected. Alarm deactivated.")

    time.sleep(0.1)
