# Demo1, read usb webcamera [2025/1/25]

How Demo1 works?
It's simple. The used funciton are:

1. `cv2.VideoCapture(0)` -- to find and return the hardware camera instance
1. `cap.isOpened()` -- to check if the hardware camera works okay
1. `cap.read()` -- to read a frame of picture form the hardware camera, and return a boolean OK status
1. `cv2.imshow("window name", frame)` -- show the fram using opencv's own window

> ![Code and interface](../90-markdown_media/Screenshot%20from%202025-01-25%2020-53-41.png)

###### Here note that the built-in opencv viewer can show the pixel value after zooming 30x.

> ![The zoom function in the built-in window](../90-markdown_media/Screenshot%20from%202025-01-25%2020-54-30.png)

# Demo2,3, read and set usb camera parameters [2025/1/25]

1.  `cv2.VideoCapture.set() or cap.set()` -- to set each parameter to the usb camera.
2.  `width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)` -- to get each parameter by name.

Common settings:

| Property                | OpenCV Constant             | Value Example   |
| ----------------------- | --------------------------- | --------------- |
| Frame Width             | `cv2.CAP_PROP_FRAME_WIDTH`  | 640, 1280       |
| Frame Height            | `cv2.CAP_PROP_FRAME_HEIGHT` | 480, 720        |
| Frames Per Second (FPS) | `cv2.CAP_PROP_FPS`          | 15, 30, 60      |
| Brightness              | `cv2.CAP_PROP_BRIGHTNESS`   | 0 - 255         |
| Contrast                | `cv2.CAP_PROP_CONTRAST`     | 0 - 255         |
| Saturation              | `cv2.CAP_PROP_SATURATION`   | 0 - 255         |
| Exposure                | `cv2.CAP_PROP_EXPOSURE`     | -1, 0, 1...     |
| Auto Focus              | `cv2.CAP_PROP_AUTOFOCUS`    | 0 (off), 1 (on) |

The currently used camera returns after running demo2.py

```json
FRAME_WIDTH: 640.0
FRAME_HEIGHT: 480.0
FPS: 30.0
BRIGHTNESS: 0.0
CONTRAST: 16.0
SATURATION: 36.0
HUE: 0.0
GAIN: Not Supported
EXPOSURE: Not Supported
FOCUS: Not Supported
AUTOFOCUS: Not Supported
WHITE_BALANCE: Not Supported
SHARPNESS: 6.0
BACKLIGHT: 1.0
GAMMA: 100.0
ZOOM: Not Supported
TILT: Not Supported
PAN: Not Supported

```

> ##### Note that usb camera does not remember the settings mostly, so you have to set your parameter everytime when you start your program.

# Demo4. showing realtime frame on webpage [2025/1/25]

- Flask will handle the web server and serve them via HTTP.
- OpenCV will capture the video frames
- See '[03-video_streaming_MIME%20type.md](./03-video_streaming_MIME%20type.md)' for how the streaming works.

Test result (by watching a stopwatch from 0~10s and check the print output of video_frame_cnt):

- when set 640\*480, the frame rate is 30hz (video_frame_cnt = 300)
- when set 1280\*720, the frame rate is 8hz (video_frame_cnt 80)

> ![running a webpage](../90-markdown_media/Screenshot%20from%202025-01-25%2022-47-52.png)
