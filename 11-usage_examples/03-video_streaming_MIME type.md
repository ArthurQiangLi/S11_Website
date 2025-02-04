# What is mimetype

> Refer to ['01-camera-read-and-set.md'](./01-camera-read-and-set.md) about how to operate the camera.

[2025/1/28]
![Alt text](../90-markdown_media/Screenshot%20from%202025-02-03%2016-54-14.png)

```python
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
```

This defines a Flask route for the URL path `0.0.0.0/vodeo_feed`. When a webpage accesses this url, Flask calls the video_feed() function above. This function returns a real-time video stream to the webpage.

How? Response() is used in Flask to send back HTTP response to webpages. It wraps/calls the generate_frames() function somewhere in the code, which streams/yields JPEG frames.
`mimetype='multipart/x-mixed-replace; boundary=frame` -- sets the MIME type to support the continuous stream of images.

What is MIMEtype? MIME stands for `Multipurpose Internet Mail Extension`. `mimetype='multipart/x-mixed-replace; boundary=frame` represents a special content type for streaming data in HTTP response. It asks for a stream instead of asking for a response , closing and restart asking. The `boundary=frame` prefixes each frame with `--frame`, telling the browser to replace the previous frame with the new one.

```py
def generate_frame():
	...
    frame = buffer.tobytes()
    yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
```

The generate_frames() outputs frames in the format:

```py
--frame
Content-Type: image/jpeg
[binary JPEG image data]

--frame
Content-Type: image/jpeg
[binary JPEG image data]
```

The html file:

```html
<html>
  <head>
    <title>Webcam Stream</title>
  </head>
  <body>
    <h1>Live Webcam Display</h1>
    <p>
      The python function 'generate_frame() is called by the webpage, it reads
      the camera and encodes the frame data into a .jpg picture. What you see in
      the webpage is actuall a refreshed jpg picture.
    </p>
    <img
      src="{{ url_for('video_feed') }}"
      width="{{width}}"
      height="{{height}}"
    />
  </body>
</html>
```
