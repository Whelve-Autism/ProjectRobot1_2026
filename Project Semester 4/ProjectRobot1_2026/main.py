# -*- coding: utf-8 -*-
# ProjectRobot1_2026
# Micro:bit Tinybit Robot Car Control
# This file contains all robot control functions used in the coursework project.

from microbit import display, Image, sleep, button_a, button_b
import tinybit

# ---------------------------------------------------------------------------
# Initialization
# ---------------------------------------------------------------------------
display.show(Image.HAPPY)

# ---------------------------------------------------------------------------
# Utility function
# ---------------------------------------------------------------------------

def clamp_speed(value):
    """
    Limit motor values to the valid range 0 to 255.
    Motor drivers on the Tinybit car expect values within this range.
    """
    if value < 0:
        return 0
    if value > 255:
        return 255
    return value


# ---------------------------------------------------------------------------
# Basic movement functions
# ---------------------------------------------------------------------------

def move_forward(duration=1000):
    """
    Move the robot forward for a given duration in milliseconds.
    Calibrated values: left motor slightly higher than right to reduce drift.
    """
    tinybit.car_run(clamp_speed(50), clamp_speed(45))
    sleep(duration)
    stop_robot()


def move_backward(duration=1000):
    """
    Move the robot backward for a given duration in milliseconds.
    Backward values are higher because reverse motion often needs more power.
    """
    tinybit.car_run(clamp_speed(225), clamp_speed(200))
    sleep(duration)
    stop_robot()


def stop_robot():
    """Stop both motors immediately."""
    tinybit.car_run(0, 0)


# ---------------------------------------------------------------------------
# Directional control functions
# ---------------------------------------------------------------------------

def turn_left(duration=700):
    """
    Turn the robot left for a given duration in milliseconds.
    Placeholder values below can be adjusted after real-world testing.
    Left motor runs slower / backward while right motor runs forward.
    """
    # Adjust these values after testing on your specific robot surface.
    tinybit.car_run(clamp_speed(30), clamp_speed(120))
    sleep(duration)
    stop_robot()


def turn_right(duration=700):
    """
    Turn the robot right for a given duration in milliseconds.
    Placeholder values below can be adjusted after real-world testing.
    Right motor runs slower / backward while left motor runs forward.
    """
    # Adjust these values after testing on your specific robot surface.
    tinybit.car_run(clamp_speed(120), clamp_speed(30))
    sleep(duration)
    stop_robot()


# ---------------------------------------------------------------------------
# Speed control
# ---------------------------------------------------------------------------

# Current speed level used by set_speed() and related functions.
CURRENT_SPEED = "medium"

# Calibrated speed presets. Right motor is slightly lower to reduce deviation.
SPEED_PRESETS = {
    "low": (30, 25),
    "medium": (50, 45),
    "high": (80, 70),
}


def set_speed(level):
    """
    Set the global speed level to low, medium, or high.
    Returns True if the level is valid, otherwise False.
    """
    global CURRENT_SPEED
    if level in SPEED_PRESETS:
        CURRENT_SPEED = level
        return True
    return False


def move_forward_with_speed(level, duration=1000):
    """
    Move forward using a selected speed level for a given duration.
    All motor values pass through clamp_speed() before use.
    """
    if level not in SPEED_PRESETS:
        stop_robot()
        return

    left_speed, right_speed = SPEED_PRESETS[level]
    tinybit.car_run(clamp_speed(left_speed), clamp_speed(right_speed))
    sleep(duration)
    stop_robot()


# ---------------------------------------------------------------------------
# Infrared line tracking / path control
# ---------------------------------------------------------------------------

def read_left_ir():
    """
    Read the left infrared line-tracking sensor.

    NOTE: Different Tinybit versions may use different infrared sensor APIs.
    Replace the placeholder return value below with the correct function from
    your Tinybit hardware documentation or from tested sensor output.

    Example placeholders (replace with your actual API):
        return tinybit.tracking_left()
        return tinybit.line_left()
        return tinybit.read_line_sensor(0)
    """
    # Placeholder: 1 = black track detected, 0 = no black track detected.
    return 0


def read_right_ir():
    """
    Read the right infrared line-tracking sensor.

    NOTE: Different Tinybit versions may use different infrared sensor APIs.
    Replace the placeholder return value below with the correct function from
    your Tinybit hardware documentation or from tested sensor output.

    Example placeholders (replace with your actual API):
        return tinybit.tracking_right()
        return tinybit.line_right()
        return tinybit.read_line_sensor(1)
    """
    # Placeholder: 1 = black track detected, 0 = no black track detected.
    return 0


def follow_black_track(runtime=10000):
    """
    Follow a black track using left and right infrared sensors.

    Logic:
    - Both sensors on black: move forward at tracking speed.
    - Left on black, right off: apply left correction.
    - Right on black, left off: apply right correction.
    - Neither on black: stop for safety.

    Uses short sampling intervals for responsive control.
    """
    # Tracking speed with a small right-motor offset to reduce deviation.
    track_forward_left = clamp_speed(40)
    track_forward_right = clamp_speed(35)
    track_left_correct = (clamp_speed(20), clamp_speed(60))
    track_right_correct = (clamp_speed(60), clamp_speed(20))

    elapsed = 0
    sample_interval = 50  # milliseconds between sensor checks

    while elapsed < runtime:
        left_on_black = read_left_ir()
        right_on_black = read_right_ir()

        if left_on_black and right_on_black:
            # Both sensors detect the black track: drive straight.
            tinybit.car_run(track_forward_left, track_forward_right)
        elif left_on_black and not right_on_black:
            # Track curves left: apply left correction.
            tinybit.car_run(track_left_correct[0], track_left_correct[1])
        elif right_on_black and not left_on_black:
            # Track curves right: apply right correction.
            tinybit.car_run(track_right_correct[0], track_right_correct[1])
        else:
            # No track detected: stop for safety.
            stop_robot()

        sleep(sample_interval)
        elapsed += sample_interval

    stop_robot()


# ---------------------------------------------------------------------------
# Traffic sign response
# ---------------------------------------------------------------------------

def respond_to_sign(sign_label):
    """
    Respond to a traffic sign label.

    The sign_label may come from:
    - a computer-side recognition program,
    - a manually selected command during testing, or
    - a future vision / camera module.

    Supported labels: left, right, speed_up, slow_down, stop, unknown
    """
    if sign_label == "left":
        turn_left()
    elif sign_label == "right":
        turn_right()
    elif sign_label == "speed_up":
        set_speed("high")
        move_forward_with_speed("high", 1000)
    elif sign_label == "slow_down":
        set_speed("low")
        move_forward_with_speed("low", 1000)
    elif sign_label == "stop":
        stop_robot()
    else:
        # Unknown sign: stop for safety.
        stop_robot()


# ---------------------------------------------------------------------------
# Computer-based remote control / command demo
# ---------------------------------------------------------------------------

def run_command(command):
    """
    Run a command from a computer-side test script or manual input.

    Supported commands:
    forward, backward, left, right, stop,
    speed_low, speed_medium, speed_high, track,
    sign_left, sign_right, sign_speed_up, sign_slow_down, sign_stop
    """
    if command == "forward":
        move_forward()
    elif command == "backward":
        move_backward()
    elif command == "left":
        turn_left()
    elif command == "right":
        turn_right()
    elif command == "stop":
        stop_robot()
    elif command == "speed_low":
        set_speed("low")
        move_forward_with_speed("low", 1000)
    elif command == "speed_medium":
        set_speed("medium")
        move_forward_with_speed("medium", 1000)
    elif command == "speed_high":
        set_speed("high")
        move_forward_with_speed("high", 1000)
    elif command == "track":
        follow_black_track()
    elif command == "sign_left":
        respond_to_sign("left")
    elif command == "sign_right":
        respond_to_sign("right")
    elif command == "sign_speed_up":
        respond_to_sign("speed_up")
    elif command == "sign_slow_down":
        respond_to_sign("slow_down")
    elif command == "sign_stop":
        respond_to_sign("stop")
    else:
        # Invalid command: stop the robot and show an error indicator.
        stop_robot()
        display.show(Image.SAD)
        print("Invalid command:", command)


# ---------------------------------------------------------------------------
# Main demonstration loop
# ---------------------------------------------------------------------------

def demo_sequence():
    """
    Demonstrate the main robot features in a safe, ordered sequence.
    Each action includes stopping or short durations to avoid runaway motion.
    """
    display.show(Image.ARROW_N)
    move_forward(800)

    display.show(Image.ARROW_S)
    move_backward(800)

    display.show(Image.ARROW_W)
    turn_left()

    display.show(Image.ARROW_E)
    turn_right()

    display.show(Image.TRIANGLE)
    move_forward_with_speed("low", 800)

    display.show(Image.SQUARE)
    move_forward_with_speed("high", 800)

    display.show(Image.ARROW_W)
    respond_to_sign("left")

    display.show(Image.ARROW_E)
    respond_to_sign("right")

    stop_robot()
    display.show(Image.HAPPY)


# ---------------------------------------------------------------------------
# Program entry point
# ---------------------------------------------------------------------------

# Keep the robot idle until a button is pressed.
stop_robot()

while True:
    display.show(Image.HAPPY)

    if button_a.was_pressed():
        demo_sequence()
    elif button_b.was_pressed():
        stop_robot()
        display.show(Image.NO)
        sleep(300)
    else:
        # Idle state: robot remains stopped for safety.
        stop_robot()
        sleep(100)
