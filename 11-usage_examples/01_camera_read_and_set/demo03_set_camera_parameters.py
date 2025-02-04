import cv2

def main():
    # Open the default camera (0 for built-in webcam, change to 1, 2, etc. for external cameras)
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Set camera parameters (adjust these values as needed)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set height
    cap.set(cv2.CAP_PROP_FPS, 30)            # Set frames per second
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 10)    # Set brightness (0-255)
    cap.set(cv2.CAP_PROP_CONTRAST, 50)       # Set contrast (0-255)
    cap.set(cv2.CAP_PROP_SATURATION, 50)     # Set saturation (0-255)
    
#    sleep(1000)
    # Dictionary of common camera properties
    properties = {
        "FRAME_WIDTH": cv2.CAP_PROP_FRAME_WIDTH,
        "FRAME_HEIGHT": cv2.CAP_PROP_FRAME_HEIGHT,
        "FPS": cv2.CAP_PROP_FPS,
        "BRIGHTNESS": cv2.CAP_PROP_BRIGHTNESS,
        "CONTRAST": cv2.CAP_PROP_CONTRAST,
        "SATURATION": cv2.CAP_PROP_SATURATION,
        "HUE": cv2.CAP_PROP_HUE,
        "GAIN": cv2.CAP_PROP_GAIN,
        "EXPOSURE": cv2.CAP_PROP_EXPOSURE,
        "FOCUS": cv2.CAP_PROP_FOCUS,
        "AUTOFOCUS": cv2.CAP_PROP_AUTOFOCUS,
        "WHITE_BALANCE": cv2.CAP_PROP_WHITE_BALANCE_BLUE_U,
        "SHARPNESS": cv2.CAP_PROP_SHARPNESS,
        "BACKLIGHT": cv2.CAP_PROP_BACKLIGHT,
        "GAMMA": cv2.CAP_PROP_GAMMA,
        "ZOOM": cv2.CAP_PROP_ZOOM,
        "TILT": cv2.CAP_PROP_TILT,
        "PAN": cv2.CAP_PROP_PAN,
    }

    print("Camera Properties:\n")
    for index, (prop, prop_id) in enumerate(properties.items(), start=1):
        value = cap.get(prop_id)
        if value == -1:  # Some properties may not be supported
            print(f"{index} {prop}: Not Supported")
        else:
            print(f"{index} {prop}: {value}")


    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the captured frame
        cv2.imshow('USB Webcam Live Feed', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()