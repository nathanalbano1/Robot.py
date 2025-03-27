from gpiozero import PWMLED, Servo, LED
import time

# Initialize RGB LED pins
r_red_pwm_pin = PWMLED(14)
r_green_pwm_pin = PWMLED(15)
r_blue_pwm_pin = PWMLED(18)

l_red_pwm_pin = PWMLED(27)
l_green_pwm_pin = PWMLED(22)
l_blue_pwm_pin = PWMLED(23)

# Initialize traffic light LEDs
red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)

# Initialize servo motor
wave_servo = Servo(21, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def stop_light(traffic_light_status):
    """Controls the traffic light LEDs based on the input status."""
    print(f"Traffic light status: {traffic_light_status}")
    if traffic_light_status["red_LED"] == 1:  # Stop
        green_led.off()
        yellow_led.on()
        time.sleep(3)
        yellow_led.off()
        red_led.on()
    else:  # Go
        red_led.off()
        green_led.on()

def wave():
    """Moves the servo motor in a waving motion."""
    print("Waving the servo motor...")
    for _ in range(3):  # Repeat waving 3 times
        wave_servo.mid()
        print("Servo at mid position")
        time.sleep(0.5)
        wave_servo.min()
        print("Servo at min position")
        time.sleep(1)
        wave_servo.mid()
        print("Servo at mid position")
        time.sleep(0.5)
        wave_servo.max()
        print("Servo at max position")
        time.sleep(1)

def eyes_RGB(Leyes_RGBs, Reyes_RGBs):
    """Controls the RGB LEDs for both eyes."""
    print("Setting RGB values for left and right eyes...")
    # Left eye
    l_red_pwm_pin.value = Leyes_RGBs["Lred_RGBLED"]
    l_green_pwm_pin.value = Leyes_RGBs["Lgreen_RGBLED"]
    l_blue_pwm_pin.value = Leyes_RGBs["Lblue_RGBLED"]
    # Right eye
    r_red_pwm_pin.value = Reyes_RGBs["Rred_RGBLED"]
    r_green_pwm_pin.value = Reyes_RGBs["Rgreen_RGBLED"]
    r_blue_pwm_pin.value = Reyes_RGBs["Rblue_RGBLED"]

def get_robot_feature_data():
    """Main function to control traffic lights, RGB LEDs, and servo motor."""
    try:
        # Traffic light status
        traffic_light_status = {"red_LED": 0, "yellow_LED": 0, "green_LED": 1}
        print("Enter traffic light status:")
        print("1 for Stop, 0 for Go")
        traffic_light_status["red_LED"] = int(input("Traffic light status (1/0): "))
        stop_light(traffic_light_status)

        # RGB LEDs for eyes
        Leyes_RGBs = {"Lred_RGBLED": 0, "Lgreen_RGBLED": 0, "Lblue_RGBLED": 0}
        Reyes_RGBs = {"Rred_RGBLED": 0, "Rgreen_RGBLED": 0, "Rblue_RGBLED": 0}

        # Get values for left eye
        print("Enter RGB values for the left eye (0.0 to 1.0):")
        Leyes_RGBs["Lred_RGBLED"] = float(input("Left Eye Red: "))
        Leyes_RGBs["Lgreen_RGBLED"] = float(input("Left Eye Green: "))
        Leyes_RGBs["Lblue_RGBLED"] = float(input("Left Eye Blue: "))

        # Get values for right eye
        print("Enter RGB values for the right eye (0.0 to 1.0):")
        Reyes_RGBs["Rred_RGBLED"] = float(input("Right Eye Red: "))
        Reyes_RGBs["Rgreen_RGBLED"] = float(input("Right Eye Green: "))
        Reyes_RGBs["Rblue_RGBLED"] = float(input("Right Eye Blue: "))

        # Set RGB values
        eyes_RGB(Leyes_RGBs, Reyes_RGBs)

        # Servo motor wave
        wave()

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Run the program
get_robot_feature_data()


