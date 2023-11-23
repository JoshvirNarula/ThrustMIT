import pyrealsense2 as rs
import numpy as np
import cv2

pipe = rs.pipeline()
cfg = rs.config()

#cfg.enable_stream(rs.stream.color, 424, 240, rs.format.bgr8, 60)
cfg.enable_stream(rs.stream.infrared, 1, 480, 270, rs.format.y8, 60)

pipe.start(cfg)

# Define the codec for RGB and infrared VideoWriters
#rgb_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
ir1_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create separate VideoWriter objects for RGB and infrared
#rgb_out = cv2.VideoWriter('output_rgb2.mp4', rgb_fourcc, 60.0, (424, 240))
ir1_out = cv2.VideoWriter('output_sphere.mp4', ir1_fourcc, 60.0, (480, 270), isColor=False)

try:
    while True:
        frame = pipe.wait_for_frames()
        #color_frame = frame.get_color_frame()
        ir1_frame = frame.get_infrared_frame(1)

        #color_image = np.asanyarray(color_frame.get_data())
        ir1_image = np.asanyarray(ir1_frame.get_data())

        # Write the frames to the respective video files
        #rgb_out.write(color_image)
        ir1_out.write(ir1_image)

        #cv2.imshow('rgb', color_image)
        cv2.imshow('ir1', ir1_image)

        if cv2.waitKey(1) == ord('q'):
            break

finally:
    # Release the VideoWriters for both RGB and infrared
    #rgb_out.release()
    # ir1_out.release()

    # Close the pipeline
    pipe.stop()

    # Close all windows
    cv2.destroyAllWindows()