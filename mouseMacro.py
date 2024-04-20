from pynput import mouse
import sys
import signal


class MouseController:
    def __init__(self):
        self.mouse_controller = mouse.Controller()
        self.button_pressed = False

    def press_button(self):
        if not self.button_pressed:
            self.mouse_controller.press(mouse.Button.right)
            self.button_pressed = True

    def release_button(self):
        if self.button_pressed:
            self.mouse_controller.release(mouse.Button.right)
            self.button_pressed = False

    def toggle_button(self):
        if self.button_pressed:
            self.release_button()
        else:
            self.press_button()


if __name__ == "__main__":
    controller = MouseController()
    action = sys.argv[1]

    if action == "press_rightButton":
        controller.toggle_button()

    # Keep the program running until it receives a stop signal
    signal.pause()
