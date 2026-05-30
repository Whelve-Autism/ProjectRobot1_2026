# ProjectRobot1_2026

## Project Description

This repository contains the coursework project for an IoT robot car demonstration using a **micro:bit** and a **Tinybit robot car kit**. The project demonstrates basic robot movement, directional control, speed control, infrared line tracking, traffic sign response, and simple computer-based command testing.

All robot control logic is implemented in a **single Python file** (`main.py`) for clarity and easy submission in an academic report.

## Hardware Components

- BBC micro:bit board
- Tinybit robot car chassis and motor driver
- Left and right DC motors
- Infrared line-tracking sensors (left and right)
- Battery pack / power supply for the robot car
- USB cable for uploading code to the micro:bit
- Optional: printed track map and miniature traffic signs for testing

## Software Tools

- [Mu Editor](https://codewith.mu/) for editing and flashing MicroPython code
- micro:bit MicroPython firmware
- Tinybit library (`import tinybit`) provided with the robot kit
- Optional: a computer-side Python script for sending test commands (future extension)
- Git and GitHub for version control and coursework submission

## Main Functions

| Function | Description |
|----------|-------------|
| `clamp_speed(value)` | Limits motor values to the range 0–255 |
| `move_forward()` / `move_backward()` | Basic forward and backward movement |
| `stop_robot()` | Stops both motors |
| `turn_left()` / `turn_right()` | Directional turning control |
| `set_speed(level)` | Sets speed level: low, medium, or high |
| `move_forward_with_speed(level)` | Forward movement at a selected speed |
| `read_left_ir()` / `read_right_ir()` | Infrared sensor wrappers (adjust for your hardware) |
| `follow_black_track()` | Line-following control loop |
| `respond_to_sign(sign_label)` | Responds to traffic sign labels |
| `run_command(command)` | Maps computer-side commands to robot actions |
| `demo_sequence()` | Demonstrates all main features in order |

## How to Upload `main.py` to the micro:bit (Mu Editor)

1. Connect the micro:bit to your computer using a USB cable.
2. Open **Mu Editor**.
3. Click **Mode** and select **BBC micro:bit**.
4. Open `main.py` from this project folder.
5. Click **Flash** to upload the code to the micro:bit.
6. Wait until the upload completes. The micro:bit display should show a happy face when idle.

## How to Test the Robot

1. Place the robot on a flat, open surface with enough space to move safely.
2. After flashing, the robot stays **stopped** until you press a button.
3. Press **Button A** to run the full `demo_sequence()` (forward, backward, turns, speeds, sign response).
4. Press **Button B** at any time to **stop** the robot immediately.
5. For individual function testing, you can temporarily call functions from the Mu REPL or add short test calls in `main.py` (remember to remove test code before submission).
6. For line tracking, update `read_left_ir()` and `read_right_ir()` with your actual sensor API, then test on a black track line.
7. For traffic sign testing, call `respond_to_sign("left")` or use `run_command("sign_left")` from a connected test script.

## Infrared Sensor API Adjustment

Different Tinybit kit versions may use different function names for infrared line sensors. The functions `read_left_ir()` and `read_right_ir()` in `main.py` are written as **wrappers** with placeholder values.

Before running `follow_black_track()`, open `main.py` and replace the placeholder return values with the correct API calls from your Tinybit documentation, for example:

```python
return tinybit.tracking_left()
return tinybit.tracking_right()
```

Test each sensor separately and confirm that `1` means black track detected and `0` means no track detected (or invert the logic if your hardware behaves differently).

## GitHub Submission Notes

- This project is designed as a **GitHub-ready coursework repository**.
- Keep all robot logic in `main.py` only (do not split into multiple Python modules).
- Use meaningful commit messages that describe each stage of development.
- See `git_commands.md` for a suggested Git command history.
- Do **not** commit private credentials, `.env` files, or local IDE settings.
- Include this README and your report screenshots or demo video link in your coursework submission as required by your module.

## Project Structure

```
ProjectRobot1_2026/
├── main.py           # All robot control logic (single file)
├── README.md         # Project documentation
├── git_commands.md   # Git command history template
└── .gitignore        # Common ignore rules
```

## Safety Notes

- Always test at low speed first.
- Keep hands clear of wheels while motors are running.
- Use `stop_robot()` or Button B to stop the robot immediately.
- The main loop keeps the robot idle until a button is pressed to avoid unexpected movement.
