import cv2

def main():
    cap = cv2.VideoCapture(0)    # Open the default camera (0 for built-in webcam, change to 1, 2, etc. for external cameras)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
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
