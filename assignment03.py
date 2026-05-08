from gpiozero import Button, MotionSensor
from picamera2 import Picamera2
from time import sleep
from signal import pause
from datetime import datetime


button = Button(2)     
pir = MotionSensor(4)    


camera = Picamera2()
camera.configure(camera.create_still_configuration())
camera.start()

print("Burglar detector started.")
print("Move in front of PIR sensor to take a photo.")
print("Press button to stop.")

def take_photo():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/home/pi/Desktop/hw01/image_{now}.jpg"

    print("Motion detected!")
    camera.capture_file(filename)
    print(f"Photo saved: {filename}")

    sleep(10)  

def stop_program():
    print("Button pressed. Stopping camera...")
    camera.stop()
    print("Program stopped.")
    exit()


pir.when_motion = take_photo
button.when_pressed = stop_program

pause()
