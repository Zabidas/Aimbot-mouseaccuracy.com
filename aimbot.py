import cv2
import pyautogui
import keyboard
import numpy as np

def find_and_click_target(target_image):
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Initialize the paused flag variable
    paused = False

    while True:
        # Check if the "l" key is pressed to pause/start the script
        if keyboard.is_pressed('l'):
            paused = not paused
            if paused:
                print("Script paused. Press 'l' to resume.")
            else:
                print("Script resumed.")

            # Wait until the 'l' key is released
            while keyboard.is_pressed('l'):
                pass

        # Break the loop if the "q" key is pressed
        if keyboard.is_pressed('q'):
            break

        if not paused:
            try:
                # Search for the target image on the screen
                screen_image = pyautogui.screenshot()
                screen_image_np = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2BGR)

                result = cv2.matchTemplate(screen_image_np, target_image, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                # Set a threshold for the match value to consider it a valid detection
                threshold = 0.6

                if max_val >= threshold:
                    # Extract the top-left corner coordinates of the target image
                    top_left_x = max_loc[0]
                    top_left_y = max_loc[1]

                    # Calculate the center coordinates of the target image
                    target_width = target_image.shape[1]
                    target_height = target_image.shape[0]
                    target_center_x = top_left_x + target_width // 2
                    target_center_y = top_left_y + target_height // 2

                    # Move the mouse cursor to the target image and click
                    pyautogui.moveTo(target_center_x, target_center_y)
                    pyautogui.click()
                else:
                    print("Target image not found on the screen.")

            except Exception as e:
                print("An error occurred:")
                print(e)

# Load the target image
target_image = cv2.imread('C:/Users/User/Desktop/aimbot v4/target/target.png')

# Pause/Start functionality
print("Press 'l' to pause/start the script. Press 'q' to quit.")

# Call the find_and_click_target function
find_and_click_target(target_image)

# Keep the script running until manually closed
while True:
    pass
