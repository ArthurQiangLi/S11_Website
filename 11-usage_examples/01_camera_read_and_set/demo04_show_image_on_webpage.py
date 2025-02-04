from flask import Flask, Response, render_template_string
import cv2

app = Flask(__name__)

SET_FRAME_WIDTH = 1280
SET_FRAME_HEIGHT = 720
video_frame_cnt = 0

# Initialize webcam (0 for default webcam, 1 for external USB camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("## Open camera successfully.")
    # Set desired camera properties (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, SET_FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, SET_FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 30)


def generate_frames():
    global video_frame_cnt
    while True:
        success, frame = cap.read()  # Read frame from webcam
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            video_frame_cnt+=1
            print(f"## Get a new frame index={video_frame_cnt}.")
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            
            # Yield the frame as part of an HTTP response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    # HTML template for streaming
    return render_template_string('''
        <html>
            <head>
                <title>Webcam Stream</title>
            </head>
            <body>
                <h1>Live Webcam Display</h1>
                <p> The python function 'generate_frame() is called by the webpage, it reads the camera and encodes the frame data into a .jpg picture. What you see in the webpage is actuall a refreshed jpg picture. </p>
                <img src="{{ url_for('video_feed') }}" width="{{width}}" height="{{height}}">
            </body>
        </html>
    ''', width=SET_FRAME_WIDTH, height=SET_FRAME_HEIGHT)
    #pass width=SET_FRAME_WIDTH, height=SET_FRAME_HEIGH parameter to html.

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False) # False or Ture does not matter.
