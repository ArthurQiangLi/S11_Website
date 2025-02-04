import cv2

def list_camera_properties():
    cap = cv2.VideoCapture(0)  # Open default camera

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

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

    cap.release()

if __name__ == "__main__":
    list_camera_properties()



