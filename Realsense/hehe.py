import cv2
import pyrealsense2 as rs
import os
import time
import numpy as np
from pynput import keyboard

# Create folders if they don't exist
os.makedirs("images/rgb", exist_ok=True)
os.makedirs("images/infrared", exist_ok=True)

# Set up RealSense pipelinqe configuration
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 424, 240)
config.enable_stream(rs.stream.infrared, 1, 480, 270)

# Start streaming
pipeline.start(config)

# Variable to keep track of the image number
image_number = 1

# Flag to control the capturing process
capturing = True

# Function to toggle capturing with the space key
def on_space_release(key):
    global capturing
    if key == keyboard.Key.space:
        capturing = not capturing
        print("Capturing Paused" if not capturing else "Capturing Resumed")

# Set up the listener for the space key
listener = keyboard.Listener(on_release=on_space_release)
listener.start()

try:
    while True:
        if capturing:
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()

            # Get frames
            color_frame = frames.get_color_frame()
            infrared_frame = frames.get_infrared_frame()

            if not color_frame or not infrared_frame:
                continue

            # Convert frames to numpy arrays
            color_image = np.asanyarray(color_frame.get_data())
            infrared_image = np.asanyarray(infrared_frame.get_data())

            # Convert RGB to BGR color space
            color_image_bgr = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)

            # Save images
            cv2.imwrite(f"images/rgb/rgb_{image_number}.png", color_image_bgr)
            cv2.imwrite(f"images/infrared/infr_{image_number}.png", infrared_image)

            # Display the saved images for 1 second
            cv2.imshow("RGB Image", color_image_bgr)
            cv2.imshow("Infrared Image", infrared_image)
            cv2.waitKey(1000)  # Wait for 1000 milliseconds (1 second)

            # Close the image windows
            cv2.destroyAllWindows()

            print(f"Images saved and displayed: rgb_{image_number}.png, infr_{image_number}.png")

            # Increment image number
            image_number += 1

except KeyboardInterrupt:
    print("Keyboard interrupt. Exiting...")

finally:
    # Stop streaming
    pipeline.stop()
    listener.stop()
    cv2.destroyAllWindows()