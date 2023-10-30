import cv2

stream_url = "rtsp://admin:ZTLBTF@192.168.1.8:554/stream"
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Can not open video")
else:
    # Read information in header
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_rate = cap.get(5)

    codec_info = int(cap.get(cv2.CAP_PROP_FOURCC))

    codec = chr(codec_info & 0xFF) + chr((codec_info >> 8) & 0xFF) + chr((codec_info >> 16) & 0xFF) + chr((codec_info >> 24) & 0xFF)


    print("Resolution: {}x{}".format(frame_width, frame_height))
    print("FPS: {:.2f} fps".format(frame_rate))
    print("Codec: {}".format(codec))

    cap.release()